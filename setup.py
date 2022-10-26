from setuptools import setup, find_packages

setup(name='pomm_ui',
      version='1.0',
      description='The POMM UI',
      url='https://github.jpl.nasa.gov/Cartography/POMM-UI',
      author='Tariq Soliman',
      author_email='tariq.k.soliman@jpl.nasa.gov',
      license='Apache License Version 2.0',
      packages=find_packages(),
      scripts=["pomm-ui.py"],
      install_requires=[
          'ttkbootstrap',
          'tkinterweb'
      ],
      include_package_data=True,
      package_data={'':['*.json', 'assets/*.png',
                        'help/*.css','help/*.html']},
      zip_safe=False)
