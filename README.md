# testable-notebook A template repo for testable jupyter notebooks

A sample notebook and corresponding test is found at:
 * notebooks/sample_notebook.ipynb
 * tests/test_sample_notebook.py

The enivronment.yml defines an environment called "testable-nb-env", you may want to 
rename it to something related to your project. 

The conda environment can be created with: ```conda env create --name my_envname --file=environment.yml```

The repo uses testbook and nbmake to test the notebook. Testbook is used to unit test individual
functions in a notebook, whereas nbmake tests the entire notebook to test that it executed successfully.

# To run tests

To run both the unit tests, and a test of the entire notebook execute the following:

```pytest ./tests && pytest --nbmake ./notebooks/```



