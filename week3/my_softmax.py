import torch
import torch.nn as nn


class MySoftmax(nn.Module):
    def __init__(self):
        super(MySoftmax, self).__init__()

    def forward(self, x):
        exp_x = torch.exp(x)
        sum_exp = torch.sum(exp_x)
        return exp_x / sum_exp


class Softmax_Stable(nn.Module):
    def __init__(self):
        super(Softmax_Stable, self).__init__()

    def forward(self, x):
        c = torch.max(x, dim=0, keepdim=True)
        exp_x = torch.exp(x - c.values)
        sum_exp = exp_x.sum(0, keepdim=True)
        return exp_x / sum_exp


def test_question1():
    data = torch.Tensor([1, 2, 3])
    softmax_function = nn.Softmax(dim=0)
    output = softmax_function(data)
    assert round(output[0].item(), 2) == 0.09
    print(output)


def test_question2():
    data = torch.Tensor([5, 2, 4])
    softmax = MySoftmax()
    output = softmax(data)
    print(output)


def test_question3():
    data = torch.Tensor([1, 2, 300000000])
    my_softmax = MySoftmax()
    output = my_softmax(data)
    assert round(output[0].item(), 2) == 0.0
    print(output)


def test_question4():
    data = torch.Tensor([1, 2, 3])
    softmax_stable = Softmax_Stable()
    output = softmax_stable(data)
    assert round(output[-1].item(), 2) == 0.67
    print(output)


if __name__ == "__main__":
    test_question1()
    test_question2()
    test_question3()
    test_question4()
