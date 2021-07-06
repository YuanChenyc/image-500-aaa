FROM public.ecr.aws/lambda/python:3.8

COPY app.py  agent-setup.exe ./
CMD ["app.handler"] 
