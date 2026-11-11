'''with open('train.csv', 'r', encoding='utf-8') as f:
    lines=f.readlines()
fixed=[lines[0]]
for line in lines[1:]:
    line=line.rstrip('\n')
    if line.startswith('""') and line.endswith('""'):
        line=line[1:-1]
    line=line.replace('""','"')
    fixed.append(line+'\n')
with open('train_fixed.csv', 'w', encoding='utf-8', newline='') as f:
    f.writelines(fixed)'''

import pandas
import numpy
df=pandas.read_csv('tested.csv')
print("Загружено:", df.shape, "строк и столбцов")
print(df.head())
n=int(input("Введите n:"))
print(df.head(n))
print(df.tail())
print(df.shape, "строк и столбцов")
print("Столбцы:", list(df.columns))
print(df.dtypes)
numeric_cols=['Age', 'Fare', 'SibSp', 'Parch']
categorical_cols=['Survived', 'Pclass', 'Sex', 'Embarked', 'Cabin']
print("Числовые:", numeric_cols)
print("Категориальные:", categorical_cols)
num_df=df[numeric_cols]
stats_table=pandas.DataFrame({
    'mean':num_df.mean(),
    'median':num_df.median(),
    'min':num_df.min(),
    'max':num_df.max(),
    'std':num_df.std()}).round(2)
print(stats_table)
print(df['Pclass'].value_counts().sort_index())
print("Уникальных портов:", df['Embarked'].nunique())
print("Все порты:", df['Embarked'].unique())
print(df.isna().sum())
missing_pct=(df.isna().mean()*100).round(2)
print(missing_pct)
print("Максимум пропусков", missing_pct.idxmax(), f"({missing_pct.max()}%)")
age_before=df['Age'].dropna()
stats_before={
    'mean':age_before.mean(),
    'median':age_before.median(),
    'min':age_before.min(),
    'max':age_before.max(),
    'std':age_before.std(),
    'count':age_before.count()}
print(stats_before)
age_median=age_before.median()
df['Age']=df['Age'].fillna(age_median)
print("Медиана", age_median)
age_after=df['Age']
stats_after={
    'mean':age_after.mean(),
    'median':age_after.median(),
    'min':age_after.min(),
    'max':age_after.max(),
    'std':age_after.std(),
    'count':age_after.count()}
print(stats_after)
comparison=pandas.DataFrame({
    'до обработки':stats_before,
    'после обработки':stats_after})
comparison.index=['Среднее','Медиана','Мин','Макс','Стд.откл.','Кол-во известных']
print(comparison.round(2))
df=df.dropna(subset=['Embarked'])
print('После удаления Embarked:', df.shape)
cabin_missing=df['Cabin'].isna().mean()
print(f"Доля пропусков Cabin:{cabin_missing:.2%}")
if cabin_missing>0.5:
    df=df.drop(columns=['Cabin'])
    print("Cabin удалён")
else:
    print("Cabin оставлен (пропусков меньше 50%)")
print(df.isna().sum())
print("Итоговая размерность:", df.shape)

df['Fare']=df['Fare'].fillna(df['Fare'].median())
print("\nПропуски после обработки Fare:")
print(df.isna().sum())
survived=df['Survived'].to_numpy()
sex=df['Sex'].to_numpy()
age=df['Age'].to_numpy()
fare=df['Fare'].to_numpy()
print(f"Выжило всего: {survived.mean()*100:.2f}%")
print("Выживаемость по полу:")
for s in ['male', 'female']:
    mask=sex==s
    print(f" {s}: {survived[mask].mean()*100:.2f}% (n={mask.sum()})")
print("Средний возраст:")
print(f"мужчины: {age[sex=='male'].mean():.2f}")
print(f"женшина: {age[sex=='female'].mean():.2f}")
print("Средний возраст по полу и выживаемости:")
for s in ['male', 'female']:
    for sv in [1, 0]:
        mask=(sex==s)&(survived==sv)
        label='выжил' if sv==1 else 'погиб'
        if mask.sum() == 0:
            print(f"    {s}, {label}: нет таких пассажиров (n=0)")
        else:
            print(f"    {s}, {label}: {age[mask].mean():.2f}  (n={mask.sum()})")
print(f"Fare: min={fare.min():.2f}, max={fare.max():.2f}, mean={fare.mean():.2f}")
print(f"Std возраста: {age.std():2f}")
summary_sex=pandas.DataFrame({
    'Мужчины':[
        survived[sex=='male'].mean()*100,
        age[sex=='male'].mean(),
        age[(sex=='male')&(survived==1)],
        age[(sex=='male')&(survived==0)]
    ],
    'Женщины':[
        survived[sex=='female'].mean()*100,
        age[sex=='female'].mean(),
        age[(sex=='female')&(survived==1)],
        age[(sex=='female')&(survived==0)]
    ]
}, index=['% выживших','Ср. возраст','Ср. возраст выживших','Ср. возраст погибших'])
print(summary_sex.round(2))
f1=df[(df['Sex']=='male')&(df['Age']>30)&(df['Pclass']==1)]
print("Задание 1. Мужчина >30 в 1ом классе", len(f1))
print(f1.head(10))
f2=df[(df['Age']<18)|((df['Sex']=='female')&(df['Survived']==1))]
print("Задание 2. дети моложе 18 или выжившие женщины:",len(f2))
avg_fare_3=df[df['Pclass']==3]['Fare'].mean()
f3=df[(df['Pclass']==3)&(df['Fare']>avg_fare_3)]
print(f"Задание 3. 3ий класс с Fare > {avg_fare_3:.2f}: {len(f3)}")
f4=df[(df['Age']>=20)&(df['Age']<=40)&(df['Embarked']=='S')]
print("Задание 4. 20-40 лет из порта S:", len(f4))
grp=df.groupby(['Pclass', 'Sex']).agg(
    count=('PassengerId','count'),
    mean_age=('Age', 'mean'),
    survived_pct=('Survived', lambda x: x.mean()*100),
    mean_fare=('Fare', 'mean')
).round(2)
print("руппировка по Pclass и Sex:")
print(grp)
port=df.groupby('Embarked').agg(
    count=('PassengerId', 'count'),
    survived_pct=('Survived', lambda x: x.mean()*100)
).round(2)
print("Группировка по Embarked:")
print(port)
by_class=(df.groupby('Pclass')['Survived'].mean()*100).round(2)
print("Доля выживших по классам:")
print(by_class)
print("Класс с наибольшей долей выживших:", by_class.idxmax())
df.to_csv('titanic_processed.csv', index=False)
print("Сохранено: titanic_processed.csv")
grp.to_csv('titanic_statististics.csv')
print("Сохранено: titanic_statististics.csv")
check=pandas.read_csv('titanic_processed.csv')
print("Проверка загрузки", check.shape)
print(check.head())
