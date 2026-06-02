from utils.preprocess import clean_text

sample = """

I know Python, SQL,

Machine Learning!!!

Visit:

http://abc.com

"""

result = clean_text(

    sample

)

print(result)