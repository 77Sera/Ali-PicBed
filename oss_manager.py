# coding:utf8

# 主要实现: 文件的上传 / 下载，返回url

try:
    import oss2
    from my_utils import *
except ImportError as e:
    print_error(e)


class OssManager:
    def __init__(self,
                 endpoint="<Your EndPoint>",
                 accesskey_id="<Your AccessKeyId>",
                 accesskey_secret="<Your AccessKeySecret>",
                 bucket_name="<Your BUCKET NAME>",
                 bucket_domain_name="<Your BucketDomainName>"):

        self.bucket_domain_name = bucket_domain_name

        auth = oss2.Auth(accesskey_id, accesskey_secret)
        self.bucket = oss2.Bucket(auth, endpoint, bucket_name)

    def upload_file(self, file, ismarkdown=False):
        '''
        :param file: string 待上传的文件名，包含路径
        :param ismarkdown: boolean 是否返回markdown格式url
        :return: 返回上传文件的url，可选markdown格式
        '''
        try:
            with open(file, 'rb') as local_file:

                remote_file = "{time}/{ram_file_name}{file_ext}".format(
                    time = get_time(),  # 获取当前日期
                    ram_file_name = get_timestamp_ram(),  # 按时间戳命名文件
                    file_ext = get_file_ext(file)  # 获取文件后缀
                )

                # 上传文件
                self.bucket.put_object(remote_file, local_file.read())

            print("[*] Upload ok - " + file)
        except oss2.exceptions.RequestError as e:
            print_error(e,other_string=
            "[!] Fail to Connect with Ali-OSS" + "|" +
            "[!] Please Check Your Config File and Try again")
        except Exception as e2:
            print_error(e2, other_string="[!] Unknow Error!" )

        target_path = "http://{0}/{1}".format(
            self.bucket_domain_name,
            remote_file
        )

        if ismarkdown: target_path = "![]({0})".format(target_path)

        return target_path