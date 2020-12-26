# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# 该默认管道无法帮助我们请求图片数据，因此该管道我们就不用
# class ImgproPipeline(object):
#     def process_item(self, item, spider):
#         return item

import scrapy
from scrapy.pipelines.images import ImagesPipeline  # 提供了对二进制数据下载功能(都可以下载，还有另外的两个管道类使用)
from scrapy.pipelines.media import MediaPipeline
from scrapy.pipelines.files import FilesPipeline


# 管道需要接受item中的图片地址和名称，然后再管道中请求到图片的数据对其进行持久化存储

class ImgsPipeLine(ImagesPipeline):
    # 根据图片地址发起请求
    def get_media_requests(self, item, info):
        # print(item)
        yield scrapy.Request(url=item['src'], meta={'item': item})

    # 返回图片名称即可
    def file_path(self, request, response=None, info=None, *, item=None):
        # 通过request获取meta(需要注意)
        item = request.meta['item']
        filePath = item['name']

        return filePath  # 只需要返回图片名称    在settings中设置了保存路径的

    # 将item传递给下一个即将被执行的管道类
    def item_completed(self, results, item, info):
        return item
