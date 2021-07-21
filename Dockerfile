FROM public.ecr.aws/lambda/python:2.7

COPY app.py  ./
CMD ["app.handler"] 
