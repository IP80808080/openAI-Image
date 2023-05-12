
import openai
openai.api_key = '# your api key #'
openai.Model.list()
openai.Image.create(
  prompt="Storm Dragon raging fire up the sky",
  n=1,
  size="1024x1024"
)
#########################  Use it in Colab #######################