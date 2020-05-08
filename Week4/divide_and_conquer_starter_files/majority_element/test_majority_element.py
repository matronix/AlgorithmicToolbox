import majority_element as me
#import logging



if __name__=='__main__':

    #a=[1,1,1,2,2,2,2,2,2,5,5,5]
    #a=[1,2,1,5,2,2,5,2,2,2,5,2]
    #a=[1,1,1,2,2,2,5,5,5,5,5,5,5]
    #a=[1,1,1,2,2,2,2,2,2,2,5,5]
    #a=[2,2,2,2,2]
    #a=[1,2,1]
    #a=[]
    #a=[10]
    #a=[2,1,3,2,2]
    #a=[1,2,1,1]
    #a=[2,2,2,3,9]
    #a.sort()
    ans = me.get_majority_element(a,0,len(a)-1)
    print("Final answer:{}".format(ans))
