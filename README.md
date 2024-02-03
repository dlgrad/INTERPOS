# INTERPOS
INTERPOS proposes the add-on neural architectures (INTERPOS-BF, INTERPOS-MF, INTERPOS-GF) to incorporate user's interaction rhythm for morphing the absolute position encodings in autoregressive recommender system design.
**Naming Convention**
1. Basic Fusion is abbreviated as BM, e.g. InterPosBM represents INTERPOS-BF
2. MLP Fusion is represented with Concat, e.g. InterPosConcat represents INTERPOS-MF
3. InterPosGatedFusion means INTERPOS-GF

**Models**
1. Python files in the model directory should go to recbole/model/sequential_recommender directory
2. InterPosBM, InterPosConcat, InterPosGatedFusion, SRInterPosBM, SRInterPosConcat and SRInterPosGatedFusion should be placed in recbole/properties/model

   
**Training**
run.py is responsible for running the training/validation/testing

**Sample Command**

'''
python run.py --model=InterPosBM --dataset=dataset_name --config=path/to/config

'''
    
