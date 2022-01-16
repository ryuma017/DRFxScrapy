from itemadapter import ItemAdapter


class CrawlerPipeline:
    def process_item(self, item, spider):
        item.save()
        return item
