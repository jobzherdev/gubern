# Микроразметка Schema.org для сайта gubernskaya-hotel.ru (Тильда)

Готовые блоки JSON-LD для:
1. **Страницы контактов** `/contacts/` — тип `Hotel` (полная карточка объекта).
2. **Блока организации на каждой странице** — тип `Organization` (бренд + юрлицо, ставится глобально).

> **Почему JSON-LD, а не микроразметка в HTML (microdata/RDFa).**
> В Тильде нельзя редактировать разметку внутри стандартных блоков, поэтому microdata (`itemscope/itemprop`) там не проставить. JSON-LD — рекомендованный Google и Яндексом формат: это отдельный `<script>`, который просто вставляется в `<head>`. Работает и в Google, и в Яндекс.Вебмастере.

---

## Статус: данные заполнены — можно публиковать

Оба блока заполнены реальными данными (адрес, телефон, логотип, фото, координаты, карта, ИНН/ОГРН, соцсети). Заглушек `ЗАПОЛНИТЬ_...` в коде не осталось.

Проверить перед публикацией стоит только одно: `openingHoursSpecification` сейчас стоит круглосуточно (00:00–23:59). Если ресепшен работает по графику — поправьте `opens`/`closes`.

> Поля `priceRange` и `aggregateRating` (цена и рейтинг) намеренно не включены — по решению заказчика.

---

## 1. Страница `/contacts/` — тип `Hotel`

**Куда вставлять в Тильде:** открыть страницу контактов → «Настройки страницы» (шестерёнка) → вкладка **«Ещё» → «HTML-код для вставки внутрь HEAD»** → вставить блок ниже → Сохранить → Опубликовать.

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Hotel",
  "@id": "https://gubernskaya-hotel.ru/#hotel",
  "name": "Гостиничный комплекс «Губернский»",
  "alternateName": "Отель Губернский Шерегеш",
  "description": "Гостиничный комплекс «Губернский» 4★ в пгт Шерегеш — 200 м от подъёмника (сектор А, гора Зелёная). Гостиница на 20 номеров, апарт-отель, ресторан «Тепло», SPA-комплекс, русская баня с банным чаном.",
  "url": "https://gubernskaya-hotel.ru/",
  "logo": "https://static.tildacdn.com/tild3832-3666-4531-a138-623935396562/logo_gubernskiy.svg",
  "image": [
    "https://static.tildacdn.com/tild3733-3831-4266-a231-633061356661/Gubernsk_239.jpg",
    "https://static.tildacdn.com/tild3838-3035-4238-a537-386264663261/YAR_6665.jpg",
    "https://static.tildacdn.com/tild6634-3963-4331-b966-646230656131/5P8A0990-2.jpg"
  ],
  "telephone": "+79617100111",
  "email": "info@gubernskaya-hotel.ru",
  "currenciesAccepted": "RUB",
  "paymentAccepted": "Наличные, банковские карты",
  "starRating": {
    "@type": "Rating",
    "ratingValue": "4"
  },
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "ул. Снежная, д. 27",
    "addressLocality": "пгт Шерегеш",
    "addressRegion": "Кемеровская область — Кузбасс",
    "postalCode": "652971",
    "addressCountry": "RU"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": "52.952566",
    "longitude": "87.958578"
  },
  "hasMap": "https://yandex.ru/maps/-/CTFIrUz4",
  "checkinTime": "14:00",
  "checkoutTime": "12:00",
  "numberOfRooms": "30",
  "openingHoursSpecification": [
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": [
        "Monday", "Tuesday", "Wednesday", "Thursday",
        "Friday", "Saturday", "Sunday"
      ],
      "opens": "00:00",
      "closes": "23:59"
    }
  ],
  "amenityFeature": [
    { "@type": "LocationFeatureSpecification", "name": "Ресторан", "value": true },
    { "@type": "LocationFeatureSpecification", "name": "SPA-комплекс (2 бассейна, хамам, сауна)", "value": true },
    { "@type": "LocationFeatureSpecification", "name": "Русская баня и банный чан", "value": true },
    { "@type": "LocationFeatureSpecification", "name": "Апарт-отель с кухней", "value": true },
    { "@type": "LocationFeatureSpecification", "name": "Wi-Fi", "value": true },
    { "@type": "LocationFeatureSpecification", "name": "Парковка", "value": true },
    { "@type": "LocationFeatureSpecification", "name": "Детская площадка", "value": true }
  ],
  "sameAs": [
    "https://yandex.ru/maps/org/11274699328",
    "https://go.2gis.com/ji8Af",
    "https://vk.com/gubernskay",
    "https://t.me/gubernskaia",
    "https://max.ru/join/uRw5rxQ07Mmtpc7dlNNerDRowD4aH4i-rcrMEYH1voQ",
    "https://dzen.ru/gubernskaia_sheregesh",
    "https://rutube.ru/channel/69816886/"
  ],
  "parentOrganization": {
    "@id": "https://gubernskaya-hotel.ru/#organization"
  }
}
</script>
```

---

## 2. Блок организации на каждой странице — тип `Organization`

Несёт бренд и **юридические реквизиты** (ООО «Губерния», ИНН, ОГРН). Ставится **один раз глобально** — тогда попадёт на все страницы автоматически.

**Куда вставлять в Тильде:** «Настройки сайта» → **«Ещё» → «HTML-код для вставки внутрь HEAD (весь сайт)»** → вставить блок ниже. Он применится ко всем страницам, отдельно на каждую вставлять не нужно.

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "@id": "https://gubernskaya-hotel.ru/#organization",
  "name": "Гостиничный комплекс «Губернский»",
  "legalName": "ООО «Губерния»",
  "url": "https://gubernskaya-hotel.ru/",
  "logo": "https://static.tildacdn.com/tild3832-3666-4531-a138-623935396562/logo_gubernskiy.svg",
  "email": "info@gubernskaya-hotel.ru",
  "telephone": "+79617100111",
  "taxID": "4217147207",
  "identifier": [
    {
      "@type": "PropertyValue",
      "propertyID": "ИНН",
      "value": "4217147207"
    },
    {
      "@type": "PropertyValue",
      "propertyID": "ОГРН",
      "value": "1124217007298"
    }
  ],
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "ул. Снежная, д. 27",
    "addressLocality": "пгт Шерегеш",
    "addressRegion": "Кемеровская область — Кузбасс",
    "postalCode": "652971",
    "addressCountry": "RU"
  },
  "contactPoint": [
    {
      "@type": "ContactPoint",
      "telephone": "+79617100111",
      "contactType": "reservations",
      "areaServed": "RU",
      "availableLanguage": "Russian"
    }
  ],
  "sameAs": [
    "https://yandex.ru/maps/org/11274699328",
    "https://go.2gis.com/ji8Af",
    "https://vk.com/gubernskay",
    "https://t.me/gubernskaia",
    "https://max.ru/join/uRw5rxQ07Mmtpc7dlNNerDRowD4aH4i-rcrMEYH1voQ",
    "https://dzen.ru/gubernskaia_sheregesh",
    "https://rutube.ru/channel/69816886/"
  ]
}
```

> `@id` у Organization (`#organization`) совпадает со ссылкой `parentOrganization` в блоке отеля — так поисковик связывает бренд, юрлицо и объект в один граф. Меняете реквизиты — правьте в обоих местах согласованно.

---

## Как проверить после публикации

1. **Google Rich Results Test** — https://search.google.com/test/rich-results (вставить URL страницы).
2. **Яндекс.Вебмастер** → «Инструменты» → «Валидатор микроразметки» — https://webmaster.yandex.ru/tools/microtest/
3. Оба должны показать типы `Hotel` и `Organization` **без ошибок** (предупреждения о необязательных полях допустимы).

## Примечания

- Формат телефона в JSON-LD — международный, без пробелов и скобок: `+79XXXXXXXXX`. На самой странице для людей можно писать красиво `+7 (XXX) XXX-XX-XX`.
- Не дублировать один и тот же тип дважды на одной странице: на `/contacts/` — блок `Hotel`; `Organization` идёт глобально и на контактах тоже появится — это нормально и не конфликтует (разные `@type` и `@id`).
- После смены домена/реквизитов обновить URL и ИНН/ОГРН в обоих блоках.
