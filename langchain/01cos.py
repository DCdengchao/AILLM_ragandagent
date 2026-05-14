import numpy as np

#计算两个向量的点积
def get_dot(vec_a,vec_b):
    if len(vec_a) != len(vec_b):
        raise ValueError("两个向量的维度不一致")
    dot_sum = 0
    for a,b in zip(vec_a,vec_b):
        dot_sum += a * b
    return dot_sum

#计算单个向量的模长
def get_norm(vec):
    sum_square = 0
    for v in vec:
        sum_square += v ** 2
    return np.sqrt(sum_square)

#余弦相似度 2个向量的点积除以它们模长的乘积
def cosine_similarity(vec_a,vec_b):
    dot_product = get_dot(vec_a,vec_b)
    norm_a = get_norm(vec_a)
    norm_b = get_norm(vec_b)
    if norm_a == 0 or norm_b == 0:
        raise ValueError("向量的模长不能为零")
    return dot_product / (norm_a * norm_b) 

if __name__ == "__main__":
    vec_a = [0.5,0.5]
    vec_b = [0.7,0.7]
    vec_c = [0.7,0.5]
    vec_d = [-0.6,-0.5]

    print("ab:",cosine_similarity(vec_a,vec_b))
    print("ac:",cosine_similarity(vec_a,vec_c))
    print("ad:",cosine_similarity(vec_a,vec_d))