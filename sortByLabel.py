import numpy as np
import urllib.request
import pickle
import gzip

key_file = {
    'train_img':'train-images-idx3-ubyte.gz',
    'train_label':'train-labels-idx1-ubyte.gz',
    'test_img':'t10k-images-idx3-ubyte.gz',
    'test_label':'t10k-labels-idx1-ubyte.gz'
}
dataset_dir = 'download\\'    #データを保存する場所

for t in ['train', 'test']:
    print('step1')
    file_path = dataset_dir + key_file[t+'_label']
    with gzip.open(file_path, 'rb') as f:
        data = np.frombuffer(f.read(), np.uint8)
        label_data = data[8:] 
    print('step2')

    image_count = 0
    for i in range(4):
        image_count = 256 * image_count + data[i+4]
    file_path = dataset_dir + key_file[t+'_img']
    with gzip.open(file_path, 'rb') as f:
        data = np.frombuffer(f.read(), np.uint8)
        image_data = data[16:].reshape(image_count, 28, 28)
    print('step3')

    sorted_data = {}
    for i in range(10):
        key_no = '{:02x}'.format(i)
        idx = [j for j in range(image_count) if label_data[j] == i]
        print(idx)
        sorted_data = image_data[idx]

        print("Going to save data in file")
        o_file = dataset_dir + 'sorted_image' + key_no + '.txt'
        print(len(sorted_data))

        #csvファイルとして保存
        np.savetxt(o_file,sorted_data, delimiter=',')
        print('step4')
