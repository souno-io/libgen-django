from django.db import models


class Files(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    filepath = models.TextField(db_column='FilePath')  # Field name made lowercase.
    archiveentry = models.TextField(db_column='ArchiveEntry', blank=True, null=True)  # Field name made lowercase.
    objecttype = models.IntegerField(db_column='ObjectType')  # Field name made lowercase.
    objectid = models.IntegerField(db_column='ObjectId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'files'


class NonFiction(models.Model):
    """
    非文学库
    查询方法：NonFiction.objects.filter(title__contains='信息')
    """
    id = models.AutoField(db_column='Id', primary_key=True, help_text='条目序号')  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=254,blank=True, null=True, help_text='标题', verbose_name='标题')  # Field name made lowercase.
    volumeinfo = models.TextField(db_column='VolumeInfo', blank=True, null=True, help_text='分卷信息', verbose_name='分卷信息')  # Field name made lowercase.
    series = models.TextField(db_column='Series', blank=True, null=True, help_text='系列', verbose_name='系列')  # Field name made lowercase.
    periodical = models.TextField(db_column='Periodical', blank=True, null=True, help_text='期刊', verbose_name='期刊')  # Field name made lowercase.
    authors = models.CharField(db_column='Authors',max_length=200, blank=True, null=True, help_text='作者', verbose_name='作者')  # Field name made lowercase.
    year = models.TextField(db_column='Year', blank=True, null=True, help_text='年份', verbose_name='年份')  # Field name made lowercase.
    edition = models.TextField(db_column='Edition', blank=True, null=True, help_text='第几版', verbose_name='第几版')  # Field name made lowercase.
    publisher = models.CharField(db_column='Publisher', blank=True,max_length=254, null=True, help_text='出版社', verbose_name='出版社')  # Field name made lowercase.
    city = models.TextField(db_column='City', blank=True, null=True, help_text='城市')  # Field name made lowercase.
    pages = models.TextField(db_column='Pages', blank=True, null=True, help_text='页数', verbose_name='页数')  # Field name made lowercase.
    pagesinfile = models.IntegerField(db_column='PagesInFile', help_text='文件页数')  # Field name made lowercase.
    language = models.CharField(db_column='Language',max_length=200, blank=True, null=True, help_text='语言', verbose_name='语言')  # Field name made lowercase.
    topic = models.TextField(db_column='Topic', blank=True, null=True, help_text='主题')  # Field name made lowercase.
    library = models.TextField(db_column='Library', blank=True, null=True, help_text='书库')  # Field name made lowercase.
    issue = models.TextField(db_column='Issue', blank=True, null=True, help_text='议题')  # Field name made lowercase.
    identifier = models.TextField(db_column='Identifier', blank=True, null=True, help_text='标识符', verbose_name='标识符')  # Field name made lowercase.
    issn = models.TextField(db_column='Issn', blank=True, null=True, help_text='国际标准刊号', verbose_name='国际标准刊号')  # Field name made lowercase.
    asin = models.TextField(db_column='Asin', blank=True, null=True)  # Field name made lowercase.
    udc = models.TextField(db_column='Udc', blank=True, null=True)  # Field name made lowercase.
    lbc = models.TextField(db_column='Lbc', blank=True, null=True)  # Field name made lowercase.
    ddc = models.TextField(db_column='Ddc', blank=True, null=True)  # Field name made lowercase.
    lcc = models.TextField(db_column='Lcc', blank=True, null=True)  # Field name made lowercase.
    doi = models.TextField(db_column='Doi', blank=True, null=True)  # Field name made lowercase.
    googlebookid = models.TextField(db_column='GoogleBookId', blank=True, null=True, help_text='谷歌刊物ID')  # Field name made lowercase.
    openlibraryid = models.TextField(db_column='OpenLibraryId', blank=True, null=True, help_text='开放书库ID')  # Field name made lowercase.
    commentary = models.TextField(db_column='Commentary', blank=True, null=True, help_text='评论', verbose_name='评论')  # Field name made lowercase.
    dpi = models.IntegerField(db_column='Dpi', blank=True, null=True, help_text='点击数', verbose_name='点击数')  # Field name made lowercase.
    color = models.TextField(db_column='Color', blank=True, null=True, help_text='颜色')  # Field name made lowercase.
    cleaned = models.TextField(db_column='Cleaned', blank=True, null=True)  # Field name made lowercase.
    orientation = models.TextField(db_column='Orientation', blank=True, null=True, help_text='取向')  # Field name made lowercase.
    paginated = models.TextField(db_column='Paginated', blank=True, null=True, help_text='分页', verbose_name='分页')  # Field name made lowercase.
    scanned = models.TextField(db_column='Scanned', blank=True, null=True, help_text='已扫描')  # Field name made lowercase.
    bookmarked = models.TextField(db_column='Bookmarked', blank=True, null=True, help_text='书签', verbose_name='书签')  # Field name made lowercase.
    searchable = models.TextField(db_column='Searchable', blank=True, null=True, help_text='可查找')  # Field name made lowercase.
    sizeinbytes = models.IntegerField(db_column='SizeInBytes', help_text='字节大小')  # Field name made lowercase.
    format = models.CharField(db_column='Format',max_length=200, blank=True, null=True, help_text='文件格式', verbose_name='文件格式')  # Field name made lowercase.
    md5hash = models.TextField(db_column='Md5Hash', blank=True, null=True, help_text='MD5哈希值', verbose_name='MD5哈希值')  # Field name made lowercase.
    generic = models.TextField(db_column='Generic', blank=True, null=True, help_text='通用')  # Field name made lowercase.
    visible = models.TextField(db_column='Visible', blank=True, null=True, help_text='可用')  # Field name made lowercase.
    locator = models.TextField(db_column='Locator', blank=True, null=True, help_text='定位器')  # Field name made lowercase.
    local = models.IntegerField(db_column='Local', blank=True, null=True)  # Field name made lowercase.
    addeddatetime = models.TextField(db_column='AddedDateTime', help_text='添加时间')  # Field name made lowercase.
    lastmodifieddatetime = models.TextField(db_column='LastModifiedDateTime', help_text='最后更新时间')  # Field name made lowercase.
    coverurl = models.TextField(db_column='CoverUrl', blank=True, null=True, help_text='覆盖链接')  # Field name made lowercase.
    tags = models.TextField(db_column='Tags', blank=True, null=True, help_text='标签', verbose_name='标签')  # Field name made lowercase.
    identifierplain = models.TextField(db_column='IdentifierPlain', blank=True, null=True, help_text='简化标识符')  # Field name made lowercase.
    libgenid = models.IntegerField(db_column='LibgenId', help_text='LibgenID')  # Field name made lowercase.
    fileid = models.ForeignKey('Files', models.DO_NOTHING, db_column='FileId', blank=True, null=True, help_text='文件ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'non_fiction'
        verbose_name = u"非小说文献"
        verbose_name_plural = verbose_name
        ordering = ['id']

    def get_down_url(self, down_id):
        down_md5 = str(self.objects.values('md5hash').get(id=down_id)['md5hash'])
        libgenid = self.objects.values('libgenid').get(id=down_id)['libgenid']
        if libgenid < 1000:
            down_libgen = '0'
        else:
            down_libgen = str(self.objects.values('libgenid').get(id=down_id)['libgenid'])[:-3] + '000'
        return down_libgen+'/'+down_md5


class Scimag(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    doi = models.TextField(db_column='Doi', blank=True, null=True)  # Field name made lowercase.
    doi2 = models.TextField(db_column='Doi2', blank=True, null=True)  # Field name made lowercase.
    title = models.TextField(db_column='Title', blank=True, null=True)  # Field name made lowercase.
    authors = models.TextField(db_column='Authors', blank=True, null=True)  # Field name made lowercase.
    year = models.TextField(db_column='Year', blank=True, null=True)  # Field name made lowercase.
    month = models.TextField(db_column='Month', blank=True, null=True)  # Field name made lowercase.
    day = models.TextField(db_column='Day', blank=True, null=True)  # Field name made lowercase.
    volume = models.TextField(db_column='Volume', blank=True, null=True)  # Field name made lowercase.
    issue = models.TextField(db_column='Issue', blank=True, null=True)  # Field name made lowercase.
    firstpage = models.TextField(db_column='FirstPage', blank=True, null=True)  # Field name made lowercase.
    lastpage = models.TextField(db_column='LastPage', blank=True, null=True)  # Field name made lowercase.
    journal = models.TextField(db_column='Journal', blank=True, null=True)  # Field name made lowercase.
    isbn = models.TextField(db_column='Isbn', blank=True, null=True)  # Field name made lowercase.
    issnp = models.TextField(db_column='Issnp', blank=True, null=True)  # Field name made lowercase.
    issne = models.TextField(db_column='Issne', blank=True, null=True)  # Field name made lowercase.
    md5hash = models.TextField(db_column='Md5Hash', blank=True, null=True)  # Field name made lowercase.
    sizeinbytes = models.IntegerField(db_column='SizeInBytes')  # Field name made lowercase.
    addeddatetime = models.TextField(db_column='AddedDateTime', blank=True, null=True)  # Field name made lowercase.
    journalid = models.TextField(db_column='JournalId', blank=True, null=True)  # Field name made lowercase.
    abstracturl = models.TextField(db_column='AbstractUrl', blank=True, null=True)  # Field name made lowercase.
    attribute1 = models.TextField(db_column='Attribute1', blank=True, null=True)  # Field name made lowercase.
    attribute2 = models.TextField(db_column='Attribute2', blank=True, null=True)  # Field name made lowercase.
    attribute3 = models.TextField(db_column='Attribute3', blank=True, null=True)  # Field name made lowercase.
    attribute4 = models.TextField(db_column='Attribute4', blank=True, null=True)  # Field name made lowercase.
    attribute5 = models.TextField(db_column='Attribute5', blank=True, null=True)  # Field name made lowercase.
    attribute6 = models.TextField(db_column='Attribute6', blank=True, null=True)  # Field name made lowercase.
    visible = models.TextField(db_column='Visible', blank=True, null=True)  # Field name made lowercase.
    pubmedid = models.TextField(db_column='PubmedId', blank=True, null=True)  # Field name made lowercase.
    pmc = models.TextField(db_column='Pmc', blank=True, null=True)  # Field name made lowercase.
    pii = models.TextField(db_column='Pii', blank=True, null=True)  # Field name made lowercase.
    libgenid = models.IntegerField(db_column='LibgenId')  # Field name made lowercase.
    fileid = models.ForeignKey('Files', models.DO_NOTHING, db_column='FileId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'scimag'
        verbose_name = u"科学文章"
        verbose_name_plural = verbose_name
        ordering = ['id']


class Fiction(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    authorfamily1 = models.TextField(db_column='AuthorFamily1', blank=True, null=True)  # Field name made lowercase.
    authorname1 = models.TextField(db_column='AuthorName1', blank=True, null=True)  # Field name made lowercase.
    authorsurname1 = models.TextField(db_column='AuthorSurname1', blank=True, null=True)  # Field name made lowercase.
    role1 = models.TextField(db_column='Role1', blank=True, null=True)  # Field name made lowercase.
    pseudonim1 = models.TextField(db_column='Pseudonim1', blank=True, null=True)  # Field name made lowercase.
    authorfamily2 = models.TextField(db_column='AuthorFamily2', blank=True, null=True)  # Field name made lowercase.
    authorname2 = models.TextField(db_column='AuthorName2', blank=True, null=True)  # Field name made lowercase.
    authorsurname2 = models.TextField(db_column='AuthorSurname2', blank=True, null=True)  # Field name made lowercase.
    role2 = models.TextField(db_column='Role2', blank=True, null=True)  # Field name made lowercase.
    pseudonim2 = models.TextField(db_column='Pseudonim2', blank=True, null=True)  # Field name made lowercase.
    authorfamily3 = models.TextField(db_column='AuthorFamily3', blank=True, null=True)  # Field name made lowercase.
    authorname3 = models.TextField(db_column='AuthorName3', blank=True, null=True)  # Field name made lowercase.
    authorsurname3 = models.TextField(db_column='AuthorSurname3', blank=True, null=True)  # Field name made lowercase.
    role3 = models.TextField(db_column='Role3', blank=True, null=True)  # Field name made lowercase.
    pseudonim3 = models.TextField(db_column='Pseudonim3', blank=True, null=True)  # Field name made lowercase.
    authorfamily4 = models.TextField(db_column='AuthorFamily4', blank=True, null=True)  # Field name made lowercase.
    authorname4 = models.TextField(db_column='AuthorName4', blank=True, null=True)  # Field name made lowercase.
    authorsurname4 = models.TextField(db_column='AuthorSurname4', blank=True, null=True)  # Field name made lowercase.
    role4 = models.TextField(db_column='Role4', blank=True, null=True)  # Field name made lowercase.
    pseudonim4 = models.TextField(db_column='Pseudonim4', blank=True, null=True)  # Field name made lowercase.
    series1 = models.TextField(db_column='Series1', blank=True, null=True)  # Field name made lowercase.
    series2 = models.TextField(db_column='Series2', blank=True, null=True)  # Field name made lowercase.
    series3 = models.TextField(db_column='Series3', blank=True, null=True)  # Field name made lowercase.
    series4 = models.TextField(db_column='Series4', blank=True, null=True)  # Field name made lowercase.
    title = models.TextField(db_column='Title', blank=True, null=True)  # Field name made lowercase.
    format = models.TextField(db_column='Format', blank=True, null=True)  # Field name made lowercase.
    version = models.TextField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    sizeinbytes = models.IntegerField(db_column='SizeInBytes')  # Field name made lowercase.
    md5hash = models.TextField(db_column='Md5Hash', blank=True, null=True)  # Field name made lowercase.
    path = models.TextField(db_column='Path', blank=True, null=True)  # Field name made lowercase.
    language = models.TextField(db_column='Language', blank=True, null=True)  # Field name made lowercase.
    pages = models.TextField(db_column='Pages', blank=True, null=True)  # Field name made lowercase.
    identifier = models.TextField(db_column='Identifier', blank=True, null=True)  # Field name made lowercase.
    year = models.TextField(db_column='Year', blank=True, null=True)  # Field name made lowercase.
    publisher = models.TextField(db_column='Publisher', blank=True, null=True)  # Field name made lowercase.
    edition = models.TextField(db_column='Edition', blank=True, null=True)  # Field name made lowercase.
    commentary = models.TextField(db_column='Commentary', blank=True, null=True)  # Field name made lowercase.
    addeddatetime = models.TextField(db_column='AddedDateTime', blank=True, null=True)  # Field name made lowercase.
    lastmodifieddatetime = models.TextField(db_column='LastModifiedDateTime')  # Field name made lowercase.
    russianauthorfamily = models.TextField(db_column='RussianAuthorFamily', blank=True, null=True)  # Field name made lowercase.
    russianauthorname = models.TextField(db_column='RussianAuthorName', blank=True, null=True)  # Field name made lowercase.
    russianauthorsurname = models.TextField(db_column='RussianAuthorSurname', blank=True, null=True)  # Field name made lowercase.
    cover = models.TextField(db_column='Cover', blank=True, null=True)  # Field name made lowercase.
    googlebookid = models.TextField(db_column='GoogleBookId', blank=True, null=True)  # Field name made lowercase.
    asin = models.TextField(db_column='Asin', blank=True, null=True)  # Field name made lowercase.
    authorhash = models.TextField(db_column='AuthorHash', blank=True, null=True)  # Field name made lowercase.
    titlehash = models.TextField(db_column='TitleHash', blank=True, null=True)  # Field name made lowercase.
    visible = models.TextField(db_column='Visible', blank=True, null=True)  # Field name made lowercase.
    libgenid = models.IntegerField(db_column='LibgenId')  # Field name made lowercase.
    fileid = models.ForeignKey('Files', models.DO_NOTHING, db_column='FileId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fiction'
        verbose_name = u"文学作品"
        verbose_name_plural = verbose_name
        ordering = ['id']


