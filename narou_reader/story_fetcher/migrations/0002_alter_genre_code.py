# Generated by Django 5.0 on 2024-06-29 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story_fetcher', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='code',
            field=models.IntegerField(choices=[(0, '未選択〔未選択〕'), (101, '異世界〔恋愛〕'), (102, '現実世界〔恋愛〕'), (201, 'ハイファンタジー〔ファンタジー〕'), (202, 'ローファンタジー〔ファンタジー〕'), (301, '純文学〔文芸〕'), (302, 'ヒューマンドラマ〔文芸〕'), (303, '歴史〔文芸〕'), (304, '推理〔文芸〕'), (305, 'ホラー〔文芸〕'), (306, 'アクション〔文芸〕'), (307, 'コメディー〔文芸〕'), (401, 'VRゲーム〔SF〕'), (402, '宇宙〔SF〕'), (403, '空想科学〔SF〕'), (404, 'パニック〔SF〕'), (9901, '童話〔その他〕'), (9902, '詩〔その他〕'), (9903, 'エッセイ〔その他〕'), (9904, 'リプレイ〔その他〕'), (9999, 'その他〔その他〕'), (9801, 'ノンジャンル〔ノンジャンル〕')], unique=True),
        ),
    ]