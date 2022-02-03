from setuptools import setup, find_packages

setup(
    name='pyqt-translucent-full-loading-screen-thread',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    package_data={'pyqt_translucent_full_loading_screen_thread.ico': ['loading.gif']},
    description='PyQt thread which overlays the translucent loading screen with label on the whole window like some generic application loading screen.',
    url='https://github.com/yjg30737/pyqt-translucent-full-loading-screen-thread.git',
    install_requires=[
        'PyQt5>=5.8'
    ]
)