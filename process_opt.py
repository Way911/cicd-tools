import csv

def process_opt(filename, target_filename):
    # filename = 'tmp/opt/20210104_sse_opt.csv'
    # target_filename = 'tmp/opt_processed/20210104_sse_opt.csv'
    row_map = {}
    with open(filename, encoding='gbk', newline='') as rf:
        reader = csv.reader(rf)
        for row in reader:
            # 行号从1开始
            if reader.line_num == 1:     
                continue
            product_id = row[4]
            instrument_id = row[0]
            exchange_id = row[1]
            old_row = row_map.get(product_id, None)
            if old_row is None or instrument_id > old_row[1]:
                row_map[product_id] = [product_id, instrument_id, exchange_id]
    header = ['ProductID', 'InstrumentID', 'ExchangeID']
    with open(target_filename, mode='w', encoding='gbk', newline='') as wf:
        writer = csv.writer(wf)
        writer.writerow(header)
        writer.writerows(row_map.values())

import os.path
opt_dir = '/Users/waynecao/git/cicd-tools/tmp/opt'
opt_dir_processed = '/Users/waynecao/git/cicd-tools/tmp/opt_processed'
# opt_dir = '/nas/future/SH/opt'
# opt_dir_processed = '/nas/future/SH/opt_processed'
for root,d_names,f_names in os.walk(opt_dir):
    for f in f_names:
        os.makedirs(os.path.join(opt_dir_processed, f[:4]), exist_ok=True)
        process_opt(os.path.join(root, f), os.path.join(opt_dir_processed, f[:4], f))