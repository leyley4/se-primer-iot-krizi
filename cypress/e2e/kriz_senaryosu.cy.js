describe('YBÜ IoT Krizi Simülasyonu E2E Testleri', () => {
  beforeEach(() => {
    // Uygulamanın çalıştığı yerel adresi veya mock UI adresini buraya girersin
    cy.visit('http://localhost:3000'); 
  });

  it('İyi Son (Kayıpsız ve Yasal Uyumlu) senaryosunu baştan sona oynar', () => {
    // 1. Giriş Ekranı
    cy.contains('Simülasyonu Başlat').click();
    
    // 2. Karar 1: İzolasyon
    cy.contains('Ağı fiziksel olarak kes').click();
    cy.get('.ai-tutor-bubble').should('contain', 'nasıl çalacak?'); // Sokratik soru kontrolü
    cy.get('input').type('Cihazlar manuel otonom moda geçer.{enter}');
    
    // 3. Karar 2: Müdahale
    cy.contains('Konsoldan Port/MAC Bazlı Mikro-Segmentasyon').click();
    cy.get('input').type('Sadece enfekte olanlar ağdan düşer, ilaç vermeye devam ederler.{enter}');
    
    // 4. Karar 3: KVKK
    cy.contains('Yedekten Dönüş ve KVKK İhlal Bildirimi').click();
    cy.get('input').type('Fidye ödenmez, yasal bildirim zorunludur.{enter}');
    
    // 5. Bitiş Ekranı Kontrolü
    cy.contains('SON A - İYİ').should('be.visible');
  });
});
