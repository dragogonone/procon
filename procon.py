1つのリストから、キーを要素番号とする辞書を作成
def list_to_dict(val_list):
  return dict(zip(range(0,len(val_list)), val_list))
