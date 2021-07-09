import csv

def process_opt(filename, target_filename):
    # filename = 'tmp/opt/20210104_sse_opt.csv'
    # target_filename = 'tmp/opt_processed/20210104_sse_opt.csv'
    product_dict = {}
    with open(filename, encoding='gbk', newline='') as rf:
        reader = csv.reader(rf)
        for row in reader:
            # 行号从1开始
            if reader.line_num == 1:     
                continue
            product = row[4]
            instrument_id = row[0]
            old_instrument_id = product_dict.get(product, None)
            if old_instrument_id is None:
                product_dict[product] = instrument_id
            else:
                product_dict[product] = instrument_id if instrument_id > old_instrument_id else old_instrument_id
    header = ['ProductID', 'InstrumentID']
    with open(target_filename, mode='a+', encoding='gbk', newline='') as wf:
        writer = csv.writer(wf)
        writer.writerow(header)
        writer.writerows(product_dict.items())

import os.path
opt_dir = '/Users/waynecao/git/cicd-tools/tmp/opt'
opt_dir_processed = '/Users/waynecao/git/cicd-tools/tmp/opt_processed'
for root,d_names,f_names in os.walk(opt_dir):
    for f in f_names:
        os.makedirs(os.path.join(opt_dir_processed, f[:4]), exist_ok=True)
        process_opt(os.path.join(root, f), os.path.join(opt_dir_processed, f[:4], f))