class emb_data():
  embedding = []
  label = []
  page = {}
  cluster = -1

  def __init__(self, embedding, label, page, cluster):
    self.embedding = embedding
    self.label = label
    self.page = page
    self.cluster = cluster

  def get_embedding(self):
    return self.embedding

  def get_label(self):
    return self.label
  
  def get_page(self):
    return self.page
  
  def get_cluster(self):
    return self.cluster