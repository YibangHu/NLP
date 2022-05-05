# NLP Final project
Here's an example script that works ok(-ish)

```
python cli/train.py \
    --model_name google/mt5-small \
    --dataset_name wmt18 \
    --dataset_config ru-en \
    --source_lang en \
    --target_lang ru \
    --weight_decay 0.01 \
    --output_dir output_dir \
    --batch_size 8 \
    --num_warmup_steps 5000 \
    --learning_rate 3e-4 \
    --num_train_epochs 1 \
    --max_train_steps 100000 \
    --eval_every 5000
```

```
python cli/train.py \
    --model_name t5-base \
    --dataset_name wmt18 \
    --dataset_config de-en \
    --source_lang en \
    --target_lang de \
    --output_dir output_dir \
    --batch_size 8 \
    --num_warmup_steps 5000 \
    --learning_rate 3e-4 \
    --num_train_epochs 1 \
    --max_train_steps 100000 \
    --eval_every 5000
```
