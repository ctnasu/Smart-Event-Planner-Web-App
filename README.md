# Akıllı Etkinlik Planlama Platformu

Bu proje, **Django framework'ü** kullanarak geliştirilmiş web tabanlı bir **Akıllı Etkinlik Planlama Platformu**'nu içermektedir. Kullanıcılar etkinlik oluşturabilir, katılabilir ve sosyal etkileşim kurabilirler. Platform, kişisel tercihlere göre öneriler sunar, etkinliklerin harita üzerinden takip edilmesini sağlar ve kullanıcı etkileşimini artırmak için mesajlaşma özellikleri sunar. Aşağıda, proje geliştirilmesinde kullanılan yöntemler ve ana bileşenler açıklanmıştır.

## İçerik
1. [Frontend Geliştirme](#frontend-geliştirme)
2. [Backend Geliştirme](#backend-geliştirme)
3. [Veritabanı Tasarımı](#veritabanı-tasarımı)
4. [Akıllı Etkinlik Öneri Sistemi](#akıllı-etkinlik-öneri-sistemi)
5. [Harita ve Rota Planlama](#harita-ve-rota-planlama)
6. [Oyunlaştırma ve Puan Sistemi](#oyunlaştırma-ve-puan-sistemi)
7. [Zaman Çakışma Algoritması](#zaman-çakışma-algoritması)
8. [Mesajlaşma Sistemi](#mesajlaşma-sistemi)
9. [Admin Paneli](#admin-paneli)

---

## Frontend Geliştirme
Frontend kısmı, kullanıcıların etkinliklere kolayca erişebileceği, etkinliklere katılabileceği ve yeni etkinlikler oluşturabileceği bir arayüz tasarlanarak geliştirilmiştir. Arayüzdeki ana bileşenler şunlardır:

- **Ana Sayfa**: Kullanıcılar önerilen etkinlikleri görebilir ve yeni etkinlikler ekleyebilirler.
- **Etkinlik Sayfası**: Kullanıcılar seçtikleri etkinliğin detaylarını görüntüleyebilir ve katılabilirler.
- **Sohbet**: Etkinliklere katılan diğer kullanıcılarla sohbet edebilecekleri bir alan.
- **Kullanıcı Profili**: Kullanıcıların katıldıkları etkinlikleri ve kişisel bilgilerini görüntüleyebilecekleri bir profil sayfası.
- **Admin Paneli**: Yöneticiler kullanıcıları ve etkinlikleri yönetebilir, düzenleyebilir veya silebilirler.
- **Harita Görünümü**: Etkinliklerin konumları harita üzerinde gösterilir, kullanıcılar etkinliklere kolayca ulaşabilirler.

Frontend, **HTML**, **CSS**, **JavaScript** ve **React** kullanılarak geliştirilmiş olup, **Django** ile entegre çalışacak şekilde yapılandırılmıştır.  

## Backend Geliştirme
Backend kısmı, kullanıcı yönetimi, etkinlik oluşturma, etkinlik öneri sistemleri, mesajlaşma ve harita entegrasyonu gibi işlemleri gerçekleştiren sunucu tarafıdır. Bu kısımda **Django framework’ü** ve **Python** dili kullanılmıştır. Backend kısmında yönetilen ana işlevler şunlardır:

- **Kullanıcı Yönetimi**: Kullanıcılar, giriş yapma, kayıt olma, şifre sıfırlama ve profillerini güncelleme işlemleri gerçekleştirebilirler.
- **Etkinlik Yönetimi**: Kullanıcılar etkinlik oluşturma, düzenleme ve silme işlemleri yapabilir. Adminler ise tüm etkinlikleri yönetebilir ve gerektiğinde etkinlikleri onaylayabilir, silebilir veya düzenleyebilir.
- **Etkinlik Öneri Sistemi**: Kullanıcılara, ilgi alanlarına, katıldıkları etkinliklere ve konumlarına göre kişiselleştirilmiş etkinlik önerileri sunan bir sistem.
- **Çakışma Algoritması**: Etkinliklerin tarih ve saatleri kontrol edilerek, çakışan etkinlikler hakkında kullanıcı bilgilendirilir.
- **Mesajlaşma Paneli**: Etkinliklere katılan kullanıcılar, etkinlik sayfası üzerinden birbirleriyle mesajlaşabilirler. Her etkinlik için ayrı bir sohbet odası oluşturulmuştur.

## Veritabanı Tasarımı
Projede **ilişkisel veritabanı** kullanılmıştır. Django ORM (Object-Relational Mapping) ile yönetilen veritabanında şu ana tablolar bulunmaktadır:

- **Kullanıcılar**: Kullanıcı adı, şifre, e-posta adresi, profil fotoğrafı gibi bilgileri içerir.
- **Etkinlikler**: Etkinlik adı, tarih, saat, açıklama ve konum bilgilerini tutar.
- **Katılımcılar**: Hangi kullanıcının hangi etkinliğe katıldığını takip eden ilişki tablosu.
- **Mesajlar**: Kullanıcılar arasındaki mesajları tutan tablo.
- **Puanlar**: Kullanıcıların etkinliklere katılım ve etkinlik oluşturma gibi aktivitelerine göre kazandıkları puanları tutar.

## Akıllı Etkinlik Öneri Sistemi
Kullanıcıların ilgi alanlarına, etkinlik geçmişlerine ve bulundukları konuma göre önerilen etkinlikler, **kural tabanlı bir algoritma** ile sunulmaktadır. Bu öneri sistemi aşağıdaki kurallara göre çalışır:

- **İlgi Alanı Uyum Kuralı**: Kullanıcının ilgi alanlarına uygun etkinlikler önerilir.
- **Katılım Geçmişi Kuralı**: Kullanıcının önceki etkinlik katılımlarına göre benzer etkinlikler önerilir.
- **Coğrafi Konum Kuralı**: Kullanıcının bulunduğu konuma yakın etkinlikler önerilir.

## Harita ve Rota Planlama
Etkinliklerin konumları **Google Maps API** kullanılarak harita üzerinde işaretlenmiş ve kullanıcılar en uygun rotayı seçebilirler. Nasıl giderim? butonuna tıklandığında etkinlik konumunun google haritalardaki bölgesini gösterir.Kullanıcılar farklı ulaşım yöntemleri (yürüyerek, araçla, bisikletle vb.) için alternatif rota seçeneklerini görebilirler.

## Oyunlaştırma ve Puan Sistemi
Etkinliklere katılımı teşvik etmek için bir **puanlama sistemi** geliştirilmiştir. Kullanıcılar etkinliklere katıldıkça, etkinlik oluşturdukça ve platforma ilk kez katıldıklarında puan kazanacaklardır. Kazanılan puanlar kullanıcı profillerinde gösterilecek ve etkinlik katılımını teşvik edecektir.

## Zaman Çakışma Algoritması
Kullanıcıların etkinliklere katılmadan önce zaman çakışmalarını önlemek amacıyla geliştirilmiş bir algoritma, kullanıcının mevcut etkinlikleri ile yeni etkinlik arasındaki zaman dilimlerini kontrol eder ve herhangi bir çakışma tespit edilirse kullanıcıyı bilgilendirir.

## Mesajlaşma Sistemi
Etkinliklere katılan kullanıcılar, etkinlik sayfası üzerinden birbirleriyle sohbet edebilirler. Her etkinlik için ayrı bir sohbet alanı oluşturulmuş ve mesajlaşma kaydedilir. Etkinliklere katılan tüm kullanıcılar bu alanda etkileşime girebilir.

## Admin Paneli
Admin paneli, yöneticilerin kullanıcıları ve etkinlikleri yönetebileceği bir alandır. Adminler, etkinlikleri onaylayabilir, düzenleyebilir veya silebilirler. Ayrıca, kullanıcı geri bildirimlerini toplama ve analiz etme işlevlerine de sahiptir.

---


https://github.com/user-attachments/assets/1e9780a0-96c3-4ef0-8e9d-b0916274c462

