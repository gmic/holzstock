from __future__ import absolute_import, unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailembeds.blocks import EmbedBlock
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore import blocks
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel
from wagtail.wagtailimages.blocks import ImageChooserBlock

COLOUR_CHOICES = [
    ('bg-white', 'Geen'),
    ('bg-primary', 'Primair'),
]


class TwoColumnBlock(blocks.StructBlock):
    background = blocks.ChoiceBlock(choices=COLOUR_CHOICES, default="bg-white")
    left_column = blocks.StreamBlock([
        ('heading', blocks.CharBlock(classname="title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('embedded_video', EmbedBlock()),
        # ('google_map', GoogleMapBlock()),
    ], icon='arrow-left', label='Left column content')

    right_column = blocks.StreamBlock([
        ('heading', blocks.CharBlock(classname="title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('embedded_video', EmbedBlock()),
        # ('google_map', GoogleMapBlock()),
    ], icon='arrow-right', label='Right column content')

    class Meta:
        template = 'holzstock/blocks/two_column_block.html'
        icon = 'placeholder'
        label = 'Two Columns'


class JumbotronBlock(blocks.StructBlock):
    image = ImageChooserBlock()
    heading = blocks.CharBlock(classname="full title")
    paragraph = blocks.RichTextBlock()

    class Meta:
        template = 'holzstock/blocks/jumbotron.html'
        icon = 'user'


class HomePage(Page):
    body = StreamField([
        ('two_columns', TwoColumnBlock()),
        ('jumbotron', JumbotronBlock()),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]
