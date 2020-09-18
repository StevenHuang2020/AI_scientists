#python3 Steven 09/18/20
'''AI/DL/CV paper list'''

from paperDict import Paper
    
papers = [] #paper list

papers.append( Paper(author = 'Geoffrey Hinton et al.', \
        year ='2012', \
        name ='Imagenet classification with deep convolutional neural networks', \
        url= 'http://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks.pdf', \
        desc = 'Imagenet classification with deep convolutional neural networks') )

papers.append( Paper(author = 'Kunihiko Fukushima', \
        year ='1980', \
        name ='Neocognitron: A self-organizing neural network model for a mechanism of visual pattern recognition', \
        url= 'https://www.rctn.org/bruno/public/papers/Fukushima1980.pdf', \
        desc = 'The original of convolutional neural networks') )

papers.append( Paper(author = 'Ian Goodfellow et al.', \
        year ='2014', \
        name ='Conditional generative adversarial nets', \
        url= 'http://papers.nips.cc/paper/5423-generative-adversarial-nets.pdf', \
        desc = 'Generative adversarial nets(GAN)') )

papers.append( Paper(author = 'Yann LeCun, Yoshua Bengio & Geoffrey Hinton', \
        year ='MAY,2015', \
        name ='Deep Learning', \
        url= 'https://s3.us-east-2.amazonaws.com/hkg-website-assets/static/pages/files/DeepLearning.pdf', \
        desc = 'Deep Learning review') )

papers.append( Paper(author = 'Papageorgiou et al.', \
        year ='1998', \
        name ='A General Framework for Object Detection', \
        url= 'https://pdfs.semanticscholar.org/3770/af50ce05a47955a94f428a28769ca33b5d26.pdf', \
        desc = 'Haar face detection') )

papers.append( Paper(author = 'VIOLA & JONES', \
        year ='SEP,2001', \
        name ='Robust Real-Time Face Detection', \
        url= 'https://link.springer.com/content/pdf/10.1023/b:visi.0000013087.49260.fb.pdf', \
        desc = 'Haar face detection real-time') )

papers.append( Paper(author = 'Dalal & Triggs', \
        year ='Jun 2005', \
        name ='Histograms of Oriented Gradients for Human Detection', \
        url= 'https://hal.inria.fr/file/index/docid/548512/filename/hog_cvpr2005.pdf', \
        desc = 'HOG Human Detection, CVPR 05') )