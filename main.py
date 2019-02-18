# coding:utf8

if __name__ == '__main__':
    from oss_manager import OssManager
    from my_utils import *

    config_file = ".config"
    configs = load_config(config_file)

    om = OssManager(
        endpoint=configs["endpoint"],
        bucket_domain_name=configs["bucket_domain_name"],
        bucket_name=configs["bucket_name"],
        accesskey_id=configs["accesskey_id"],
        accesskey_secret=configs["accesskey_secret"]
    )

    target_path = om.upload_file("test/test_data/test.png", ismarkdown=True)

    print(target_path)
