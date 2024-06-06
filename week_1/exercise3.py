import random
import math

def exercise3(num_samples, loss_name: str, y, yh):
    
    if not isinstance(num_samples, int):
        print("num_samples must be a int")
        return
    
    if num_samples < 0:
        print("num_samples must be greater than zero")
        return

    lower_loss_name = loss_name.lower()
    if lower_loss_name != 'mae' and lower_loss_name != 'mse' and lower_loss_name != 'rmse':
        print(f'Loss function {loss_name} is not supported.')
        return
    
    if lower_loss_name == 'mae':
        sum = 0
        for i in range(num_samples):
            sum += abs(y[i] - yh[i])
            loss = sum / (i + 1)
            print(f'loss name: {loss_name}, sample: {i}, pred: {yh[i]}, target: {y[i]}, loss: {loss}')
        final_loss = sum / num_samples
    elif lower_loss_name == 'mse':
        sum = 0
        for i in range(num_samples):
            temp = abs(y[i] - yh[i])
            sum += temp * temp
            loss = sum / (i + 1)
            print(f'loss name: {loss_name}, sample: {i}, pred: {yh[i]}, target: {y[i]}, loss: {loss}')
        final_loss = sum / num_samples
    else:
        sum = 0
        for i in range(num_samples):
            temp = abs(y[i] - yh[i])
            sum += temp * temp
            loss = sum / (i + 1)
            print(f'loss name: {loss_name}, sample: {i}, pred: {yh[i]}, target: {y[i]}, loss: {loss}')
        final_loss = math.sqrt(sum / num_samples)
    
    print(f'Final loss {final_loss}')


def calc_ae(y, y_hat):
    return abs(y - y_hat)


def calc_se(y, y_hat):
    err = (y - y_hat)
    return err * err


if __name__ == '__main__':
    num_sample = 5
    y = random.sample(range(0, 10), num_sample)
    yh = random.sample(range(0, 10), num_sample)
    exercise3(num_samples=num_sample, loss_name='mse', y=y, yh=yh)
