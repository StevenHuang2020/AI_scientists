#python3 Steven 09/17/20
'''scientists list'''
#https://www.kdnuggets.com/2019/09/12-deep-learning-research-leaders.html

from personDict import Scientist
    
scientists = [] #Scientist list
#--------------------------------Geoffrey Hinton---------------------------#
Hinton = Scientist(name='Geoffrey Hinton',
        desc = 'University of Toronto & Engineering Fellow, Google',\
        googleScholar = 'https://scholar.google.com/citations?user=JicYPdAAAAAJ&hl=en&oi=ao',\
        fields = 'Machine learning,Neural networks,Artificial intelligence,Cognitive science,Object recognition',
        wiki = 'https://en.wikipedia.org/wiki/Geoffrey_Hinton',\
        website = 'http://www.cs.toronto.edu/~hinton/')

Hinton.addPapers('Imagenet classification with deep convolutional neural networks',\
    'http://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks.pdf')
scientists.append(Hinton)

#--------------------------------Kunihiko Fukushima---------------------------#
Fukushima = Scientist(name='Kunihiko Fukushima',
        desc = 'Kyoto University',\
        googleScholar = '',\
        fields = 'Artificial neural networks, Neocognitron, CNN architecture, Unsupervised learning, Deep learning',
        wiki = 'https://en.wikipedia.org/wiki/Kunihiko_Fukushima')

Fukushima.addPapers('Neocognitron: A self-organizing neural network model for a mechanism of visual pattern recognition',\
    'https://www.rctn.org/bruno/public/papers/Fukushima1980.pdf')
scientists.append(Fukushima)

#--------------------------------Andrew Ng------------------------------------#
Andrew_Ng = Scientist(name='Andrew Ng',
        desc = 'Stanford University & Google Brain',\
        googleScholar = 'https://scholar.google.com/citations?user=mG4imMEAAAAJ&hl=en&oi=ao',\
        fields = 'Artificial intelligence, machine learning, natural language processing, computer vision',
        wiki = 'https://en.wikipedia.org/wiki/Andrew_Ng',\
        website = 'http://www.cs.stanford.edu/~ang')

scientists.append(Andrew_Ng)


#--------------------------------Ian Goodfellow------------------------------------#
Ian_Goodfellow = Scientist(name='Ian Goodfellow',
        desc = 'Stanford University & Apple Inc. & Google Brain & OpenAI',\
        googleScholar = 'https://scholar.google.com/citations?user=iYN86KEAAAAJ&hl=en&oi=ao',\
        fields = 'Computer science, GAN',
        wiki = 'https://en.wikipedia.org/wiki/Ian_Goodfellow',\
        website = 'www.iangoodfellow.com')

Ian_Goodfellow.addPapers('Conditional generative adversarial nets',\
    'https://arxiv.org/pdf/1411.1784.pdf')

scientists.append(Ian_Goodfellow)

#--------------------------------Yoshua Bengio------------------------------------#
Yoshua_Bengio = Scientist(name='Yoshua Bengio',
        desc = r'Université de Montréal',\
        googleScholar = 'https://scholar.google.com/citations?user=iYN86KEAAAAJ&hl=en&oi=ao',\
        fields = 'Deep learning, neural machine translation, generative adversarial networks,"attention model", word embeddings, denoising auto-encoders, neural language models, learning to learn',
        wiki = 'https://en.wikipedia.org/wiki/Yoshua_Bengio',\
        website = 'http://www.iro.umontreal.ca/~bengioy/')

scientists.append(Yoshua_Bengio)

#--------------------------------Yann LeCun------------------------------------#
Yann_LeCun = Scientist(name='Yann LeCun',
        desc = 'New York University & Chief AI Scientist, Facebook',\
        googleScholar = 'https://scholar.google.com/citations?user=WLN3QrAAAAAJ&hl=en&oi=ao',\
        fields = 'Deep learning',
        wiki = 'https://en.wikipedia.org/wiki/Yann_LeCun',\
        website = 'http://yann.lecun.com/')

Yann_LeCun.addPapers('Deep Learning',\
    'https://s3.us-east-2.amazonaws.com/hkg-website-assets/static/pages/files/DeepLearning.pdf')
Yann_LeCun.addPapers('Handwritten digit recognition with a back-propagation network',\
    'http://papers.nips.cc/paper/293-handwritten-digit-recognition-with-a-back-propagation-network.pdf')
scientists.append(Yann_LeCun)


#--------------------------------Fei-Fei Li------------------------------------#
Fei_Fei_Li = Scientist(name='Fei-Fei Li',
        desc = 'Stanford University & Google',\
        googleScholar = 'https://scholar.google.com/citations?user=rDfyQnIAAAAJ&hl=en&oi=ao',\
        fields = 'Computer vision,Machine learning,Artificial intelligence,Cognitive neuroscience',
        wiki = 'https://en.wikipedia.org/wiki/Fei-Fei_Li',\
        website = 'http://www.iro.umontreal.ca/~bengioy/')

Fei_Fei_Li.addPapers('Imagenet: A large-scale hierarchical image database',\
    'https://www.researchgate.net/profile/Li_Jia_Li/publication/221361415_ImageNet_a_Large-Scale_Hierarchical_Image_Database/links/00b495388120dbc339000000/ImageNet-a-Large-Scale-Hierarchical-Image-Database.pdf')

scientists.append(Fei_Fei_Li)


#--------------------------------Andrej Karpathy------------------------------------#
#Andrej Karpathy, Senior Director of Artifical Intelligence at Tesla.

#--------------------------------Demis Hassabis-------------------------------------#
#Demis Hassabis, Founder and CEO of DeepMind.

#--------------------------------Jeremy P. Howard------------------------------------#
#Jeremy P. Howard, Founding Researcher at fast.ai, 
# Distinguished Research Scientist at the University of San Francisco.

#--------------------------------Ruslan Salakhutdinov------------------------------------#
#Ruslan Salakhutdinov, Associate Professor at Carnegie Mellon University, Director of AI Research at Apple.
