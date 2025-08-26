import polars as pl

df = pl.DataFrame({
    "Nome": ["Ana", "Bruno", "Carla"],
    "Idade": [23, 35, 29],
    "Altura": [1.65, 1.80, 1.70],
    "Cidade": ["São Paulo", "Rio de Janeiro", "Belo Horizonte"],
    "Estado": ["SP", "RJ", "MG"]
})

print(df)
print(df.shape)
print()
# Filtrando pessoas com idade maior que 25
df_filtrado = df.filter(pl.col("Idade") > 25)
print(df_filtrado)

# Adicionando uma nova coluna com o sexo:

df = df.with_columns([
    pl.when(pl.col("Nome").is_in(["Ana", "Carla"]))
    .then(pl.lit("Feminino"))
    .otherwise(pl.lit("Masculino"))
    .alias("Sexo")
])

print()
print(df)

df.write_csv("pessoas.csv")
df.write_parquet("pessoas.parquet")
df.write_json("pessoas.json")

df2 = pl.read_csv("pessoas.csv")


novas_linhas = pl.DataFrame({
    "Nome": ["Daniel", "Eva", "João"],
    "Idade": [30, 22, 27],
    "Altura": [1.75, 1.60, 1.59],
    "Cidade": ["Curitiba", "Salvador", "Santo André"],
    "Estado": ["PR", "BA", "SP"],
    "Sexo": ["Masculino", "Feminino", "Masculino"]
})

df2 = pl.concat([df2, novas_linhas],how="vertical")
print (df2)
df2.write_csv("pessoas.csv")
df2.write_parquet("pessoas.parquet")
df2.write_json("pessoas.json")


import polars as pl

# Leitura preguiçosa
df_lazy = pl.scan_csv("pessoas.csv")

# Aplicando transformações (ainda não executadas)
df_filtrado = df_lazy.filter(pl.col("Idade") > 25)

# Executando o plano e coletando os dados
df_resultado = df_filtrado.collect()

print(df_resultado)
