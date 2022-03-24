
from dataset.data import *
from optim.regression import *
from utils.draw_tools import *
from utils.toolbox import LOGGER
from config.config import *


def reg_single(m, is_high, is_bad):

    if is_bad:
        LOGGER.info('Regression Model(Contain Bad Point, High Temp)')
        save_path = SAVE_ROOT + 'reg_bad_m_' + str(m) + '.png'
        optimizer = OptimalSolution(X_RAW, X_ADD, BAD_HIGH_TEMP, m)
        optimizer.extension_X()
        optimizer.get_w()
        print('m={},\nw={}'.format(m, optimizer.w))
        print('Img Path: {}'.format(save_path))
        draw_regression(optimizer.w, X_RAW, BAD_HIGH_TEMP, save_path)
    
    else:

        if is_high:
            LOGGER.info('Regression Model(Without Bad Point, High Temp)')
            save_path = SAVE_ROOT + 'reg_high_m_' + str(m) + '.png'
            optimizer = OptimalSolution(X_RAW, X_ADD, HIGH_TEMP, m)
            optimizer.extension_X()
            optimizer.get_w()
            print('m={},\nw={}'.format(m, optimizer.w))
            print('Img Path: {}'.format(save_path))
            draw_regression(optimizer.w, X_RAW, HIGH_TEMP, save_path)

        
        else:
            LOGGER.info('Regression Model(Without Bad Point, Low Temp)')
            save_path = SAVE_ROOT + 'reg_low_m_' + str(m) + '.png'
            optimizer = OptimalSolution(X_RAW, X_ADD, LOW_TEMP, m)
            optimizer.extension_X()
            optimizer.get_w()
            print('m={},\nw={}'.format(m, optimizer.w))
            print('Img Path: {}'.format(save_path))
            draw_regression(optimizer.w, X_RAW, LOW_TEMP, save_path)
    

def compare():

    for dim in range(1, M_MAX+1):

        save_path = SAVE_ROOT + 'reg_compare_m_' + str(dim) + '.png'
        optimizer_bad = OptimalSolution(X_RAW, X_ADD, BAD_HIGH_TEMP, dim)
        optimizer_bad.extension_X()
        optimizer_bad.get_w()
        optimizer_good = OptimalSolution(X_RAW, X_ADD, HIGH_TEMP, dim)
        optimizer_good.extension_X()
        optimizer_good.get_w()
        draw_compare(optimizer_good.w, optimizer_bad.w, X_RAW, HIGH_TEMP, BAD_HIGH_TEMP, save_path)

def get_solution():

    LOGGER.info('Draw Sample Data')
    print('data path:')
    print('{}\n{}\n{}'.format(SAVE_ROOT+'sample_high.png',SAVE_ROOT+'sample_low.png',SAVE_ROOT+'sample_bad.png'))
    draw_sample(X_RAW, HIGH_TEMP, SAVE_ROOT+'sample_high.png')
    draw_sample(X_RAW, LOW_TEMP, SAVE_ROOT+'sample_low.png')
    draw_sample(X_RAW, BAD_HIGH_TEMP, SAVE_ROOT+'sample_bad.png')

    LOGGER.info('Regression Model Start')
    for is_bad in [True, False]:
        for is_high in [True, False]:
            for dim in range(1, M_MAX+1):
                reg_single(dim, is_high, is_bad)
    
    compare()



if __name__ == '__main__':
    LOGGER.info('Start')
    get_solution()
    LOGGER.info('Done.')