from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def write_protofolio(request):
    return HttpResponse('''
<h1 style = "font-size: 80px">Menna Alhusseini</h1>
<h2 style = "font-size: 50px">AI Engineer</h2>
<p>AI Engineer specialized in designing and developing
intelligent solutions powered by data analytics and
machine learning. I excel at transforming complex
challenges into practical, innovative systems that
enhance efficiency and enable data-driven decision
making</p>
<h2>About Me</h2>
<p>I am an AI Engineer and Computer Science
student specializing in data analysis and machine
learning. I am passionate about developing
intelligent solutions that improve quality of life in
smart cities and support data-driven decision
making. My goal is to bridge advanced
technologies with real-world applications to
create impactful and sustainable innovations.</p>
<h2>Education</h2>
<p>Minia University
Faculty of computers and
information
2024 - 2027(Expected)</p>
<p>Bachelor’s degree student in Artificial
Intelligence. Gaining strong knowledge in data
analysis, machine learning, and intelligent
systems, with a focus on applying AI to real
world problems.</p>
<h2>Skills</h2>
<ul>
<li>programming: python, SQL</li>
<li>Machine learning & Deep learning</li>
<li>Data analysis & visualization </li>
<li>Neural Networks (tensorFlow / Keras)</li>
<li>Big data basics</li>
<li>Databases</li>
</ul>
<h2>Work Experience</h2>
<p>Summer Intern – Web Development & Machine Learning 2025 | [NTI]</p>
<p>Developed a website that predicts restaurant ratings based on user inputs.</p>
<p>Applied machine learning models to improve prediction accuracy</p>
<p>Gained hands-on experience in web development and data-driven applications</p>
''')
