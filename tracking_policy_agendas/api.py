"""
API
....................................................................................................
MIT License
Copyright (c) 2021-2023 AUT Iran, Mohammad H Forouhesh
Copyright (c) 2021-2022 MetoData.ai, Mohammad H Forouhesh
....................................................................................................
This module contains tools to download resources over http connections.
supported http links are:
    - https://github.com/MohammadForouhesh/crf-pos-persian/releases/download/v2.0.0.alpha/UPC_full_model_wapiti
    - https://github.com/MohammadForouhesh/crf-pos-persian/releases/download/v2.0.0.alpha/perpos.model
    - https://github.com/MohammadForouhesh/crf-pos-persian/releases/download/v2.0.0.alpha/corrections.txt
"""

import os
from typing import Union

import requests
import zipfile
from io import BytesIO

http_dict = {'xgb_vaccine': 'https://github.com/MohammadForouhesh/tracking-policy-agendas/releases/download/v1.0.0/xgb_vaccine',
             'pa_vaccine': 'https://github.com/MohammadForouhesh/tracking-policy-agendas/releases/download/v1.0.0/pa_vaccine',
             'lasso_vaccine': 'https://github.com/MohammadForouhesh/tracking-policy-agendas/releases/download/v1.0.0/lasso_vaccine',
             'gnb_vaccine': 'https://github.com/MohammadForouhesh/tracking-policy-agendas/releases/download/v1.0.0/gnb_vaccine'}


def downloader(path: str, save_path: str, mode: str) -> Union[int, None]:
    """
    A tool to download and save files over https.
    :param path:        The path to the desired file.
    :param save_path:   The intended storage path.
    :param mode:        The mode that it should be stored.
    :return:            If the file exists, it returns 0 (int), otherwise nothing would be returned.
    """
    if os.path.isfile(save_path): return 0
    try:
        model_bin = requests.get(path, allow_redirects=True)
        with zipfile.ZipFile(BytesIO(model_bin.content)) as resource:
            resource.extractall(save_path)
    except Exception:
        raise Exception('not a proper webpage')


def get_resources(dir_path: str, resource_name: str) -> str:
    """
    A tool to download required resources over internet.
    :param dir_path:        Path to the https link of the resource
    :param resource_name:   Resource name.
    :return:                Path to the downloaded resource.
    """
    save_dir = dir_path + f'/model_dir/{resource_name}'
    os.makedirs(save_dir, exist_ok=True)
    downloader(path=http_dict[resource_name], save_path=save_dir, mode='wb')
    return str(save_dir + resource_name)
