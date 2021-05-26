Longitudinal Preprocessing
--------------------------

.. raw:: html

    <div class="flowchart-container"><object data="../_static/flowcharts/longitudinal.svg" type="image/svg+xml"></object></div>

Background
^^^^^^^^^^
Longitudinal preprocessing pipeline is designed to process longitudinal data with two or more sessions. Based on `Reuter et al. 2012 <https://www.sciencedirect.com/science/article/pii/S1053811912002765?via%3Dihub>`_, all secions of subjects are first preprocessed independently and then a within-subject template is created by averaging all sessions of the subject. Subsequently the within-subject template is registered to standard space and all sections are then registered to the longitudinal template in standard space.


Configuring CPAC to Run Longitudinal Preprocessing Pipeline
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. figure:: /_images/longitudinal.png

#. **Longitudinal - [On, Off]:**  Run longitudinal preprocessing pipeline or not. Default is Off.
#. **Average Method - [string]:** Method to average longitudinal template. Default is median.
#. **DOF - [integer]:**  Transform degree of freedom in flirt. Default is 12.
#. **Interpolation - [string]:** Interpolation in flirt. Default is trilinear.
#. **Cost Function - [string]:** Cost function in flirt. Default is corratio.
#. **Thread Pool - [integer]:**  Number of threads in a thread pool. More threads can speed up the longitudinal template creation process. Default is 2.
#. **Convergence Threshold - [integer]:** Convergence threshold of longitudinal template. Default is -1, which uses numpy.finfo(np.float64).eps.

.. include:: /user/pipelines/without_gui.rst

.. literalinclude:: /references/default_pipeline.yml
   :language: YAML
   :lines: 162-194

References
^^^^^^^^^^
Martin Reuter, Nicholas J.Schmansky, H. Diana Rosas, Bruce Fischl. `Within-subject template estimation for unbiased longitudinal image analysis. <https://www.sciencedirect.com/science/article/pii/S1053811912002765?via%3Dihub>`_ Neuroimage. 2012 July 16; 61(4): 1402–1418. doi:10.1016/j.neuroimage.2012.02.084.