#FIX THE LINE BELOW
class MyStr(str):     
    def exclaim(self,num):
        return self+'!'*num

    def replace(self, take_out, use_this):
        return self.lower().replace(take_out,use_this)
                                    
        #lower.str = self.lower()
        #the_answer = lower_str.replace(take_out,use_this)
        #return the_answer
        
    
        #################
        #Make this method work in the way described in
        #the block comment above.
        #Hints:
        # 1. Remember that self is a MyStr object,
        #    and a MyStr object is also a str.
        #    However, remember that to call the replace
        #    method of str, you may need to use super
        # 2. The following str methods will be helpful:
        #       replace, lower, and upper
        # 3. There are multiple solutions, but you can
        #       do this in as little as 1 line.
        #YOUR CODE BELOW:
        #################
        
