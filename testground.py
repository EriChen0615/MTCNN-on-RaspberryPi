import numpy as np

def update_bbox(total_boxes,new_box,coord):
    co_box = np.array([[coord[0],coord[1],coord[2],coord[3]]]) # to make it of shape (1,5) to concatenate later
    for i in range(total_boxes.shape[0]):
        if _contain(co_box,total_box[i])
            if len(new_box) != 0:
                total_boxes = np.concatenate((total_boxes[:i],new_box,total_boxes[i+1:]))
            else:
                total_boxes = np.concatenate((total_boxes[:i],total_boxes[i+1:]))
            return total_boxes
    return np.concatenate(total_boxes,new_box)
        
        
def iou(a,b):
    wa = a[2]-a[0]+1
    ha = a[3]-a[1]+1
    wb = b[2]-b[0]+1
    hb = b[3]-b[1]+1
    #print("wa,ha,wb,hb",wa,ha,wb,hb)
    total_area = wa*ha+wb*hb
    #print("total_area=",total_area)
    wt = max(a[2],b[2])-min(a[0],b[0])+1
    ht = max(a[3],b[3])-min(a[1],b[1])+1 
    #print("total width and height=",wt,ht)
    inter = (wa+wb-wt)*(ha+hb-ht)
    #print("inter=",inter)
    return inter/(total_area-inter)

def _contain(a,b):
	# check if b is contained in a
	return b[0]>=a[0] and b[1]>=a[1] and b[2]<=a[2] and b[3]<=a[3]
	
if __name__ == '__main__':
	bbox_a = np.array([1,1,10,10,0.9])
	bbox_b = np.array([1,1,9,9,0.9])
	print(iou(bbox_a,bbox_b))
	print(_contain(bbox_a,bbox_b))
