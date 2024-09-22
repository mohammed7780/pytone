# from setuptools import setup, find_packages

# setup(
#     name="my_project",  # اسم المشروع
#     version="0.1",  # رقم الإصدار
#     packages=find_packages(),  # يبحث عن كل حزم المشروع تلقائيًا
#     install_requires=[],  # المتطلبات الخارجية (مكتبات أخرى يحتاجها المشروع)
#     author="Your Name",  # ضع اسمك هنا
#     author_email="email@example.com",  # ضع بريدك الإلكتروني هنا
#     description="A simple Python project on Ubuntu",  # وصف المشروع
#     url="https://github.com/username/my_project",  # رابط المشروع على GitHub
#     classifiers=[
#         "Programming Language :: Python :: 3",
#         "License :: OSI Approved :: MIT License",  # نوع الرخصة (MIT على سبيل المثال)
#         "Operating System :: OS Independent",
#     ],
#     python_requires='>=3.6',  # يحدد إصدار بايثون المطلوب (يمكن تغييره)
# )
from setuptools import setup, find_packages

setup(
    name="my_project",
    version="0.1",
    packages=find_packages(),
    install_requires=[],  # أي متطلبات خارجية هنا
    entry_points={
        'console_scripts': [
            'greet=my_project.my_module:main_function',  # استخدم المسار الكامل
        ],
    },
)
