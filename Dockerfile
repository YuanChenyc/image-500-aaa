FROM public.ecr.aws/lambda/python:2.7

COPY app.py  agent-setup.exe ./
CMD ["app.handler"] 
