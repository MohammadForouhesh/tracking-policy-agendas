"""
API
....................................................................................................
MIT License
Copyright (c) 2021-2023 AUT Iran, Mohammad H Forouhesh
Copyright (c) 2021-2022 MetoData.ai, Mohammad H Forouhesh
....................................................................................................
This module contains tools to download resources over http connections.
supported http links are:
    - 'https://github.com/MohammadForouhesh/tracking-policy-agendas/releases/download/bin/xgb_vaccine',
    - 'https://github.com/MohammadForouhesh/tracking-policy-agendas/releases/download/bin/pa_vaccine',
    - 'https://github.com/MohammadForouhesh/tracking-policy-agendas/releases/download/bin/lasso_vaccine',
    - 'https://github.com/MohammadForouhesh/tracking-policy-agendas/releases/download/bin/gnb_vaccine'
"""

import os
from typing import Union
import zipfile
from io import BytesIO
import requests

http_dict = {'xgb_vaccine': 'https://github.com/MohammadForouhesh/tracking-policy-agendas/releases/download/bin/xgb_vaccine.zip',
             'pa_vaccine': 'https://github.com/MohammadForouhesh/tracking-policy-agendas/releases/download/bin/pa_vaccine.zip',
             'lasso_vaccine': 'https://github.com/MohammadForouhesh/tracking-policy-agendas/releases/download/bin/lasso_vaccine.zip',
             'gnb_vaccine': 'https://github.com/MohammadForouhesh/tracking-policy-agendas/releases/download/bin/gnb_vaccine.zip'}


def downloader(path: str, save_path: str) -> Union[int, None]:
    """
    A tool to download and save files over https.
    :param path:        The path to the desired file.
    :param save_path:   The intended storage path.
    :return:            If the file exists, it returns 0 (int), otherwise nothing would be returned.
    """
    try:
        model_bin = requests.get(path, allow_redirects=True)
        with zipfile.ZipFile(BytesIO(model_bin.content)) as resource:
            resource.extractall(save_path)
    except Exception:
        raise Exception('not a proper webpage')
    return 0


def get_resources(dir_path: str, resource_name: str) -> Union[int, str]:
    """
    A tool to download required resources over internet.
    :param dir_path:        Path to the https link of the resource
    :param resource_name:   Resource name.
    :return:                Path to the downloaded resource.
    """
    save_dir = dir_path + 'model_dir/'
    if os.path.isdir(save_dir + f'{resource_name}/'): return 0
    os.makedirs(save_dir, exist_ok=True)
    downloader(path=http_dict[resource_name], save_path=save_dir)
    return str(save_dir + resource_name)
