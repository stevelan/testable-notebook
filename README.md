# testable-notebook A template repo for testable jupyter notebooks

A sample notebook and corresponding test is found at:
 * notebooks/sample_notebook.ipynb
 * tests/test_sample_notebook.py

The enivronment.yml defines an environment called "testable-nb-env", you may want to 
rename it to something related to your project. 

The conda environment can be created with: ```conda env create --name testable-nb-env --file=environment.yml```

The repo uses testbook and nbmake to test the notebook. Testbook is used to unit test individual
functions in a notebook, whereas nbmake tests the entire notebook to test that it executed successfully.

# To run tests
```pytest --nbmake```

To run just the unit tests:
```pytest tests/```

To execute the notebook and check for failuers:
```pytest --nbmake notebooks/```




