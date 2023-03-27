## EAI6980 Capstone Project

To run the Jupyter notebook associated with this project, first clone this repository, navigate into the newly cloned directory, create a virtual environment and activate it.

```
git clone https://github.com/cwperks/EAI6980.git
cd EAI6980
virtualenv venv
source venv/bin/activate
```

If `virtualenv` is not installed then install it using:

```
pip3 install virtualenv
```

Next, install the project dependencies:

```
pip3 install -R requirements.txt
```

Add the virtualenv as an available kernel for jupyter. The `--prefix` in the command below is the path to the virtual environment. You can use `which python3` in an activated virtualenv and remove `/bin/python3` from the end of the path
 
```
python -m ipykernel install --user --name=venv
```

The step above to create a new kernel can be repeated for each AutoML library as they each have a different set of dependencies that can clash.

To see visualizations of the keras Neural Networks you must also install graphviz. On a Mac you can use homebrew and execute:

```
brew install graphviz
```

Once all of the project dependencies are installed, run the jupyter notebook:

```
python3 -m jupyter notebook
```

Make sure the command above is preceded with `python3 -m` to ensure its running in the context of the currently activated virtualenv

### Autogluon

Installation instructions for AutoGluon can be found [here](https://auto.gluon.ai/stable/install.html).