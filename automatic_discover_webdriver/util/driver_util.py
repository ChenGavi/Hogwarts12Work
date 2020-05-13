import json
import os
import zipfile
import shutil
import requests
import pathlib
from win32com import client as win_client


def auto_download_driver(brower_path, browser_name="Chrome"):
    browser_maj_ver = get_browser_major_version(brower_path)
    latest_browser_ver = get_latest_browser_version(browser_maj_ver)
    mapping_dict = read_driver_mapping_json()

    # json为空或版本号不在mapping_dict中
    if mapping_dict is None or browser_maj_ver not in mapping_dict:
        download_browser_driver(latest_browser_ver, browser_name="Chrome")
        write_driver_mapping_json(browser_maj_ver, latest_browser_ver)
        unzip_driver(browser_maj_ver)
        remove_driver_zip()


# 工程目录
project_dir = str(pathlib.Path.cwd().parent)
CHROME_DRIVER_BASE_URL = "https://chromedriver.storage.googleapis.com"
EDGE_DRIVER_BASE_URL = "https://msedgedriver.azureedge.net"
EDGE = "https://msedgedriver.azureedge.net/81.0.416.72/edgedriver_win64.zip"
BROWSER_DRIVER_DIR = str(pathlib.PurePath(project_dir, "driver"))
DRIVER_MAPPING_FILE = os.path.join(project_dir, "config", "mapping.json")


def get_browser_version(file_path):
    """
    获取浏览器版本
    :param file_path: 浏览器文件路径
    :return: 浏览器版本号
    """
    # 判断路径文件是否存在
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"{file_path} is not found.")
    win_obj = win_client.Dispatch('Scripting.FileSystemObject')
    version = win_obj.GetFileVersion(file_path)

    return version.strip()


def get_browser_major_version(file_path):
    """
    获取浏览器主版本标识
    :param file_path: 浏览器文件路径
    :return: 浏览器主版主标识
    """
    browser_ver = get_browser_version(file_path)
    browser_major_ver = browser_ver.split(".")[0]

    return browser_major_ver


def get_latest_browser_version(browser_major_ver):
    """
    获取匹配大版本的最新release版本
    :param browser_major_ver: 浏览器主版本标识
    :return: 最新release版本号
    """
    latest_api = f"{CHROME_DRIVER_BASE_URL}/LATEST_RELEASE_{browser_major_ver}"
    resp = requests.get(latest_api)
    latest_driver_version = resp.text.strip()

    return latest_driver_version


def download_browser_driver(latest_driver_version, browser_name="Chrome"):
    """
    下载浏览器驱动压缩包
    :param browser_name: 浏览器名称
    :param latest_driver_version: 浏览器的版本号
    """
    download_api = None
    if browser_name == "Chrome":
        download_api = f"{CHROME_DRIVER_BASE_URL}/{latest_driver_version}/chromedriver_win32.zip"
    elif browser_name == "Edge":
        download_api = f"{EDGE_DRIVER_BASE_URL}/{latest_driver_version}/edgedriver_win64.zip"
    elif browser_name == "Firefox":
        pass
    else:
        pass

    download_dir = os.path.join(str(BROWSER_DRIVER_DIR), os.path.basename(download_api))
    resp = requests.get(download_api, stream=True)

    if resp.status_code == 200:
        with open(download_dir, 'wb') as fo:
            fo.write(resp.content)
    else:
        raise Exception("Download chrome driver failed")


def unzip_driver(browser_major_ver):
    """
    解压驱动压缩包
    :param browser_major_ver: 浏览器主版本号
    """
    file_path = os.path.join(BROWSER_DRIVER_DIR, os.path.basename("chromedriver_win32.zip"))
    browser_driver_dir = os.path.join(BROWSER_DRIVER_DIR, browser_major_ver)
    print(browser_driver_dir)
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(browser_driver_dir)


def remove_driver_zip():
    """
    删除下载的驱动压缩包
    """
    file_path = os.path.join(BROWSER_DRIVER_DIR, os.path.basename("chromedriver_win32.zip"))
    os.remove(file_path)


def write_driver_mapping_json(browser_major_ver, latest_driver_version, browser_name="Chrome"):
    """"""
    mapping_dict = {
        browser_major_ver:
            {
            browser_name:
                {
                    "driver_path": BROWSER_DRIVER_DIR,
                    "driver_version": latest_driver_version
                }
            }
        }
    mapping_dict.update(mapping_dict)
    with open(DRIVER_MAPPING_FILE, 'w') as fo:
        json.dump(mapping_dict, fo)


def read_driver_mapping_json():
    """
    读取 maping_json 内容
    :param file_path: json文件路径
    :return: 字典格式内容
    """
    if os.path.exists(DRIVER_MAPPING_FILE):
        with open(DRIVER_MAPPING_FILE) as fo:
            try:
                driver_mapping_dict = json.load(fo)
            # mapping.json内容为空时，返回None
            except json.decoder.JSONDecodeError:
                driver_mapping_dict = None
        # 不存在mapping.json时，返回None
    else:
        raise FileNotFoundError(f"{DRIVER_MAPPING_FILE} is not found")

    return driver_mapping_dict


def delete_driver():
    """
    清空下载的驱动文件及json配置
    """
    with open(DRIVER_MAPPING_FILE, 'w') as fo:
        fo.seek(0)
        fo.truncate()

    shutil.rmtree(BROWSER_DRIVER_DIR)
    os.mkdir(BROWSER_DRIVER_DIR)


if __name__ == '__main__':
    auto_download_driver(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
    # delete_driver()



