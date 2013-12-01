import json
# import tweetcollector
import cosine
import os
import random
import matplotlib

def read_data(filename):
    """
    Used to read all tweets from the json file.
    """
    data = []
    try:
        with open(filename) as f:
            for line in f:
                data.append(json.loads(line.strip()))
    except:
        print "Failed to read data!"
        return []
    print "The json file has been successfully read!"
    return data

class Cluster():
    def __init__(self):
    	# put your final clustering results 
    	# in the variable self.results with the format
    	# {index of cluster: [doc_id]} 
        # e.g. {1:[4,46], 2:[0,11,13,14,15,37,58],...}
        self.results_id = {}
    	# e.g. {1:["Houston rockets","houston texans"], 2:["dallas cowboys","jerry jones"],...}
        self.results = {}
        self.documents = [] # 1068 docs, doc format: {"facilityID":666666, "state": "CA", "amenity":["xxx", "aaa",...]}, ...
        self.searcher = cosine.Search()
    
    def index_documents(self, docs):
        """
        docs have 1068 docs
        return a list of doc vector, [{'a': 1.23, 'tamu': 2, ..},{...}]
        """

        # for idx,doc in enumerate(docs):
        #     d = {}
        #     d["id"] = idx
        #     d["text"] = ""
        #     for tweet in doc:
        #         d["text"] += tweet["text"]
        #     self.documents.append(d)
        print 'start index'
        print docs[0]
        # self.documents.extend(docs) #get the copy of docs
        self.searcher.index_tweets(docs)
        # for  self.searcher.vec_docs
        for idx, vector in enumerate(self.searcher.vec_docs):
            dic = {"vector":vector}
            self.documents.append(dic)
            # self.documents[idx]["vector"] = vector
        print docs[0]

    def euclidean_dist_square(self, doc_a, doc_b): #calculate euclidean distance for two vector a and b
        # doc_a = {'a': 0.xxx, 'aa':1.xx, ...}
        dist_square = sum((doc_a[x]-doc_b[x])**2 for x in doc_a if x in doc_b)
        dist_square += sum(doc_a[x]**2 for x in doc_a if x not in doc_b)
        dist_square += sum(doc_b[x]**2 for x in doc_b if x not in doc_a)
        return dist_square

    def RSS(self, cluster, centroid): # cluster is a list
        if len(cluster) == 1:
            return 0
        sum_dist = sum([self.euclidean_dist_square(centroid, c) for c in cluster])
        return sum_dist/len(cluster)

    def get_centroid(self, cluster):
        length = len(cluster)
        # print length
        if length == 1:
            return cluster[0]
        s = set()
        centroid = {}
        for vec in cluster:
            s = s | set(vec.keys())
        for word in s:
            centroid[word] = sum([vec[word] for vec in cluster if word in vec])/length
        return centroid

    def get_shift(self, centroid1, centroid2):
        """ calculate shift, centroid is a list of vec_dict...
        """
        shift = 0.0
        for idx in xrange(len(centroid1)):
            shift += sum([abs(centroid1[idx][w]-centroid2[idx][w]) for w in centroid1[idx] if w in centroid2[idx]])
            shift += sum([centroid1[idx][w] for w in centroid1[idx] if w not in centroid2[idx]])
            shift += sum([centroid2[idx][w] for w in centroid2[idx] if w not in centroid1[idx]])
        return shift

    def optimizeKmeans(self, N, k = 6, use_cosSIM = False):
        """re-run kmeans for N times to get the lowest RSS and 
           its associated results
        """
        results,totalRSS = self.kmeans(k, use_cosSIM = use_cosSIM)
        for iteration in xrange(N-1):
            res, trss = self.kmeans(k, use_cosSIM = use_cosSIM)
            if use_cosSIM == False:
                if trss < totalRSS:
                    totalRSS = trss
                    results = res
            else:
                if trss > totalRSS:
                    totalRSS = trss
                    results = res
        self.results_id = dict(results)
        return results,totalRSS

    def kmeans(self, k, use_cosSIM = False):
        """Dependancy: after index_documents or return None"""
        if self.documents is None:
            return None
        clusters = []
        results  = {}
        #random select k vectors from all vectors
        doc_vectors = [ d["vector"] for d in self.documents ]
        int_documents = random.sample(doc_vectors, k)
        for iteration in xrange(10):
            # centroids is empty
            if iteration == 0:
                centroids = int_documents
            else:
                old_centr =  list(centroids)
                for i in range(k): 
                    centroids[i] = self.get_centroid(clusters[i])
                shift = self.get_shift(old_centr, centroids)
                # print "shift", shift
                if shift < 0.001:
                    break
            # clear clusters
            clusters=[]
            for d in xrange(k):
                results[d] = []
                clusters.append([])
            # clustering :
            for idx, document in enumerate(doc_vectors):
                # append each document to closest cluster
                dist = []
                for centroid in centroids:
                    if use_cosSIM:
                        dist.append(self.searcher.CosineSim(document,centroid))
                        cluster_id = dist.index(max(dist))
                    else:
                        dist.append(self.euclidean_dist_square(document,centroid))
                        cluster_id = dist.index(min(dist))

                # cluster_id is the id of the closest cluster
                clusters[cluster_id].append(document)  # put the document in the closest cluster
                results[cluster_id].append(idx)        # put the document_id int the result
            # print "current clusters..."
            RSSes = [self.RSS(clusters[i], centroids[i]) for i in xrange(len(centroids))]
            # print sum(RSSes)
        RSSes = [self.RSS(clusters[i], centroids[i]) for i in xrange(len(centroids))]
        totalRSS = sum(RSSes)
        # print totalRSS 
        return results, totalRSS

def translateRes(result, docs):
    Parkclusters = []
    for i in result:
        clusters = {i : []}
        for idx in result[i]:
            # if i not in clusters:
            #     clusters[i] = docs[idx]
            # else:
            clusters[i].append(docs[idx])
        Parkclusters.append(clusters)
    return Parkclusters

        
if __name__ == "__main__":
    docs = read_data(os.path.join(os.getcwd(),'parkDetails.json')) 
    cluster = Cluster()
    cluster.index_documents(docs)
    results, totalRSS = cluster.optimizeKmeans(5, k = 5, use_cosSIM = True)
    # print results
    # print totalRSS
    Parkclusters = translateRes(results, docs)
    filename = "parkclusters.json"
    f = open(filename, "w")
    for c in Parkclusters:
        f.write(json.dumps(c)+'\n')
    f.close()




