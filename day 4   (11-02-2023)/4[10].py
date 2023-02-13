 claclass solution:
    def__init__(self):
        self.scrambles={}
    def is scramble(self,s1:str,s2:str)->bool:
        if(s1,s2)in self.scrambles:
            return self.scrambles[(s1,s2)]
        ifs1==s2:
            self.scrambles[(s1,s2)]=true
            return true
        ls=len(s1)
        if ls==1 or sorted(s1)!=sorted(s2):
            self.scramble[(s1,s2)]=false
            return false

        for i in range(1,ls):
            
            s1_left,s1_right=s1[:i],s1[i:]
            s2_left,s2_right=s2[:i],s2[:i]
            match1=self.isscrmble(s1_left,s2_left) and self.isscramble(s1_right2)

            s2_left2,s2_right2=s2[:ls-i],s2[ls-i:]
            match=self.isscramble(s1_left,s2_right2) and self.isscramble(s1_right2)

            if match1 or match2:
                self.scrambles[(s1,s2)]=true
                return true

            self.scrambles[(s1,s2)]=false
            return false
        
