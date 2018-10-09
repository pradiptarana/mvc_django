# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def home(request):
    # return render(request, 'blog/post_list.html', {})
    html = '<!DOCTYPE html>\
        <html>\
        <!--head start-->\
        <head>\
            <title>Home</title>\
            <link href="/static/css/index.css" type="text/css" rel="stylesheet">\
        </head>\
        <!--head end-->\
        <!--body start-->\
        <body>\
            <!--header start-->\
            <div class="header"> \
                <h1>Home</h1> \
                <nav class="navigasi">' + '<a href="/">Home</a>\
                    <a href="/about">About</a>\
                </nav>\
            </div> \
            <!--header end-->\
            <!--tentang_saya start-->\
            <div class="konten tentang center grey"> \
                <h2>Welcome to our site</h2>\
            </div> \
        </body>\
        <!--body end-->\
        </html>\
        '

    return HttpResponse(html)

def about(request):
    # return render(request, 'blog/post_list.html', {})
    html = '<!DOCTYPE html>\
        <html>\
	<head>\
        <title>Tugas-1: Mengenal HTML & CSS</title>\
        <link href="/static/css/index.css" type="text/css" rel="stylesheet">\
	</head>\
	<body>\
		<div id="header">\
			<!-- Header Logo -->\
			<div class="header-logo">\
				<p>NAMA PESERTA</p>\
			</div>\
			<!-- Header Navigation -->\
			<div class="header-nav">\
				<ul>\
					<li>\
						<a href="#">Home</a>\
					</li>\
					<li>\
						<a href="#" class="active">About</a>\
					</li>\
				</ul>\
			</div>\
		</div>\
		<div id="content">\
			<!-- Begin: About Me -->\
			<div class="about-me">\
				<h1>Tentang Saya</h1>\
				<p>Saya adalah anak pertama dari 10 bersaudara. Toni saat ini bekerja di <a href="https://www.sepulsa.com" target="_blank">SEPULSA</a> sebagai <span class="highlight">frontend developer</span>. Toni memiliki passion & kecepatan yang sangat tinggi dalam menyelesaikan pekerjaannya.</p>\
				<p>Asli Malang dan tinggal di Malang. Belum menikah.</p>\
			</div>\
			<!-- End: About Me -->\
			<!-- Begin: Hobi -->\
			<div class="my-hobby">\
				<h1>Hobi Saya</h1>\
				<p>Hobi saya lumayan banyak, diantaranya:</p>\
				<ul>\
					<li>Makan</li>\
					<li>Membaca</li>\
					<li>Main Bola</li>\
				</ul>\
			</div>\
			<!-- End: Hobi -->\
			<!-- Begin: Pendidikan -->\
			<div class="my-education">\
				<h1 class="custom-title">Pendidikan Saya</h1>\
				<ol>\
					<li>\
						SDN 123 Malang\
						<br/><span>Tahun lulus : 2008</span>\
					</li>\
					<li>\
						SMP 456 Malang\
						<br/><span>Tahun lulus : 2011</span>\
					</li>\
					<li>\
						SMA 789 Malang\
						<br/><span>Tahun lulus : 2014</span>\
					</li>\
				</ol>\
			</div>\
			<!-- End: Pendidikan -->\
		</div>\
		<!-- End: Body Container -->\
		<!-- Begin: Footer -->\
		<div id="footer">\
			<p>&copy; <a href="https://academy.alphatech.id/" target="_blank">Alphatech</a> 2018</p>\
		</div>\
		<!-- End: Footer -->\
	</body>\
</html>\
        '

    return HttpResponse(html)

def home(request):

    return render(request, 'blog/blog.html')

