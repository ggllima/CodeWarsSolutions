# For this exercise you will be strengthening your page-fu mastery. 
# You will complete the PaginationHelper class, 
# which is a utility class helpful for querying paging information related to an array.

# The class is designed to take in an array of values and an integer indicating how many items will be allowed per each page. 
# The types of values contained within the collection/array are not relevant.

# The following are some examples of how this class is used:

# helper = PaginationHelper(['a','b','c','d','e','f'], 4)
# helper.page_count() # should == 2
# helper.item_count() # should == 6
# helper.page_item_count(0)  # should == 4
# helper.page_item_count(1) # last page - should == 2
# helper.page_item_count(2) # should == -1 since the page is invalid

# # page_index takes an item index and returns the page that it belongs on
# helper.page_index(5) # should == 1 (zero based index)
# helper.page_index(2) # should == 0
# helper.page_index(20) # should == -1
# helper.page_index(-10) # should == -1 because negative indexes are invalid

class PaginationHelper():
    def __init__(self, collection, integer):
        self.collection = collection
        self.integer = integer
        
    def split_list(self):
        return [self.collection[index:index+self.integer] for index in range(0, len(self.collection), self.integer)]
        
    def page_count(self):
        
        return len(self.split_list())
        
    def item_count(self):
        return len(self.collection)
    
    def page_item_count(self, page):
        
        try:
            return len(self.split_list()[page])
        except IndexError:
            return -1
        
        
    def page_index(self,index):
        
        if index < 0:
            return -1
        else:
            try:
                element = self.collection[index]
                for indice in self.split_list():
                    if element in indice:
                        return self.split_list().index(indice)
            except IndexError:
                return -1