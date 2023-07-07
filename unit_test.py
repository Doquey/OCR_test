import argparse
from easyocr_test import predict_image




if __name__=='__main__':
    parser =argparse.ArgumentParser(description='Text detection and recognition on an image')
    parser.add_argument('-img_path',type=str, help='path to the input image')
    parser.add_argument('-l','--languages',nargs='+',default=['en','pt'])
    parser.add_argument('-d','--detail',default=True,type=bool,help='True for bounding boxes, False to just text')

    args = parser.parse_args()
    predict_image(args.img_path,args.languages,args.detail)