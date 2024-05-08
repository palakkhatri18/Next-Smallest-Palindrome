class Solution:


	def generateNextPalindrome(self,num, n ) :
            sum=0
            sum= ("".join(map(str, num[:n+1])))
            
            odd= n%2
            nod=n//2
            
            # 999999999
            def all9(sum,n):
                for i in range(0,n):
                    if sum[i]!='9':
                        return 0
                return 1
                
            if all9(sum,n)==True:
                sum='1'
                for i in range(1,n):
                    sum+="0"
                sum=sum +"1"
                return sum

            # To set center
            if odd ==0:
                center=num[nod-1]
            else:
                center=num[nod]
            
             
            left=sum[:nod]
            if odd==0:
                raright =sum[nod:]
            else:
                raright =sum[nod+1:]
                
            # 6787656
            if center!=9:
                if odd==0:
                    if raright <left[nod-1::-1]:
                        right=left[::-1]
                        return left+right
                    else:
                        left = str(int(left)+1)
                        right=left[::-1]
                        return left+right
                else:
                    if raright<left[nod-1::-1]:
                        # return left[nod::-1]
                        right=left[::-1]
                        return left + str(center) +right
                    else:
                        
                        right=left[::-1]
                    return left + str(center+1) +right
             

        # for number like 2349432 if center is 9      
            else:
                
                if odd==0:
                    if raright<left[nod-1::-1]:
                        right=left[::-1]
                        return left+right
                    else:
                        left=int(left)
                        left+=1
                        left = str(left)
                        right=left[::-1]
                        return left+right
                else:
                    if raright<left[nod-1::-1]:
                        right=left[::-1]
                        return left+str(center)+right
                    else:
                        left=int(left)
                        left+=1
                        left = str(left)
                        right=(left[::-1])
                        return str (left+'0'+right)
	        