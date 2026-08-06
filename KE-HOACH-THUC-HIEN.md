# KẾ HOẠCH THỰC HIỆN REDESIGN WEBSITE COACHHABUI.COM

> Lập ngày 06/08/2026. Thực hiện **lần lượt theo thứ tự** — mỗi giai đoạn có đầu ra rõ ràng và điểm duyệt trước khi sang giai đoạn kế.
> Tài liệu nội dung gốc: [TONG-HOP-REDESIGN.md](TONG-HOP-REDESIGN.md) · Phương án design: thư mục `design-options/`

---

## GIAI ĐOẠN 0 — Chốt phương án & dữ liệu đầu vào ⏳ ĐANG Ở ĐÂY

| # | Việc | Người quyết |
|---|---|---|
| 0.1 | ✅ **ĐÃ CHỐT (06/08/2026): Phương án B — Rừng Đêm, đan xen section sáng kem vàng nhẹ** (nhịp tối–sáng: hero/số liệu/quote/CTA dark · 2 luồng/chương trình trên nền kem). Bản B+C bị loại. Xem `design-options/B-home.html` | ✔ Xong |
| 0.2 | Chốt email chính thức: `coachhabui@gmail.com` vs `contact@coachhabui.com` | Khách hàng |
| 0.3 | Bổ sung giá + nội dung: **Chuyển Hóa Tâm** (giá, số phiên), **CoachVenture Circle** (giá, lịch), lịch khai giảng 2026 các khoá | Khách hàng |
| 0.4 | Đích của nút "Đặt lịch khai vấn" (Calendly? Google Form? Zalo?) | Khách hàng |
| 0.5 | Thu thập ảnh chất lượng cao (chân dung, retreat, lớp học) + 3 file PDF lead magnet + logo gốc | Khách hàng |
| 0.6 | Chốt stack website: giữ WordPress (đổi theme) hay build tĩnh/Next.js mới | Bạn |

**Đầu ra:** 1 phương án design được chốt + bộ dữ liệu đầy đủ.
*Ghi chú: 0.2–0.5 không chặn Giai đoạn 1–2 (dùng placeholder, điền sau).*

---

## GIAI ĐOẠN 1 — Design System (1 buổi)

1.1. Từ phương án đã chốt, cố định **design tokens**: bảng màu (hex), type scale (font/cỡ/weight), spacing, radius, shadow.
1.2. Bộ **component chuẩn**: nav (desktop + mobile menu), footer, nút (3 biến thể), card chương trình, card testimonial, section head, form đăng ký, badge chứng chỉ, khối lead magnet.
1.3. Quy ước 2 luồng: mỗi luồng ("Dành cho bạn" / "Dành cho Coach") có dấu hiệu nhận diện riêng (màu phụ/icon) dùng nhất quán toàn site.

**Đầu ra:** 1 trang style-guide HTML trong project design.
✅ **XONG (06/08/2026):** `site/style-guide.html` — đã đồng bộ lên Claude Design project (`CoachHaBui Style Guide.dc.html`).

---

## GIAI ĐOẠN 2 — Design đủ các trang (làm lần lượt, duyệt từng trang)

Thứ tự ưu tiên (trang có đủ nội dung nhất làm trước):

✅ **HOÀN THÀNH 06/08/2026** — toàn bộ 12 trang đã design xong trong `site/` (build từ `site/_build/src/` bằng `python3 site/_build/build.py`; CSS chung: `site/assets/base.css`):

| # | Trang | File | Ghi chú |
|---|---|---|---|
| 2.1 | Home (IA 2 luồng) | `site/index.html` | ✅ |
| 2.2 | Về Với Mình | `site/ve-voi-minh.html` | ✅ đủ nội dung PDF 2026 |
| 2.3 | CoachVenture Empowering | `site/coachventure-empowering.html` | ✅ kèm FAQ 5 câu |
| 2.4 | Deep-Dive Coach Training | `site/deep-dive.html` | ✅ lịch khai giảng [CHỜ XÁC NHẬN] |
| 2.5 | Về tôi | `site/ve-toi.html` | ✅ 4 vai trò, số liệu PDF |
| 2.6 | Inner Gym | `site/inner-gym.html` | ✅ 7 nguyên tắc + 6 lưu ý |
| 2.7 | Chuyển Hóa Tâm | `site/chuyen-hoa-tam.html` | ✅ giá [CHỜ XÁC NHẬN] |
| 2.8 | CoachVenture Circle | `site/coachventure-circle.html` | ✅ giá + lịch [CHỜ XÁC NHẬN] |
| 2.9 | Podcast | `site/podcast.html` | ✅ chỗ embed Spotify |
| 2.10 | Tài liệu | `site/tai-lieu.html` | ✅ 3 lead magnet + form |
| 2.11 | ~~Blog~~ | — | ⏭ SKIP theo quyết định 06/08/2026 |
| 2.12 | CV Cares | `site/cv-cares.html` | ✅ |
| 2.13 | Liên hệ | `site/lien-he.html` | ✅ form + 3 cách bắt đầu |

Đã kiểm tra tự động toàn bộ: thẻ HTML cân, nhịp band tối–sáng xen kẽ đúng (không 2 band cùng loại liền nhau), link nội bộ không gãy. Đồng bộ lên Claude Design: ⏭ SKIP theo quyết định 06/08/2026 (2 file Home B + Style Guide đã đẩy trước đó vẫn nằm trong project).

---

## GIAI ĐOẠN 3 — Build website thật

3.1. Dựng khung theo stack đã chốt (0.6):
- **Nếu WordPress:** convert design thành theme (block theme hoặc Elementor/Bricks tuỳ khách quen dùng) — khách tự sửa nội dung được.
- **Nếu tĩnh/Next.js:** dựng repo, component hoá theo design system, nội dung qua markdown/CMS nhẹ (khuyến nghị nếu muốn tốc độ + không cần khách tự sửa nhiều).

3.2. Build lần lượt theo đúng thứ tự Giai đoạn 2 (trang nào duyệt xong build trang đó).
3.3. Tích hợp: form đăng ký (đích đã chốt 0.4), form thu email lead magnet, embed Spotify/YouTube, Facebook link, mã chuyển khoản/QR nếu cần.
3.4. **Migrate blog**: chuyển 10 bài từ web cũ, phân loại lại danh mục (Inner Freedom · Nghề Coach · Đào tạo).

**Đầu ra:** website chạy trên môi trường staging.

---

## GIAI ĐOẠN 4 — Nội dung thật & SEO

4.1. Thay toàn bộ placeholder bằng ảnh thật (0.5), tối ưu dung lượng (WebP).
4.2. SEO cơ bản: title/meta description từng trang (tiếng Việt), Open Graph, schema Person + Course, sitemap.xml.
4.3. **Redirect 301** từ URL cũ → URL mới (đặc biệt 10 bài blog + các trang dịch vụ đang có traffic).
4.4. Analytics (GA4) + Facebook Pixel nếu khách chạy ads.

**Đầu ra:** staging đầy đủ nội dung thật, SEO sẵn sàng.

---

## GIAI ĐOẠN 5 — Kiểm thử & Go-live

5.1. Kiểm thử: mobile thật (iOS/Android), tốc độ (Lighthouse ≥ 90), form gửi được, mọi link sống, tiếng Việt không lỗi font.
5.2. Khách hàng duyệt lần cuối trên staging.
5.3. Trỏ domain coachhabui.com → site mới, giữ site cũ backup 30 ngày.
5.4. Theo dõi 1 tuần sau go-live: 404, form, tốc độ.

**Đầu ra:** website mới chạy chính thức trên coachhabui.com.

---

## Nguyên tắc chung

- **PDF là nguồn chuẩn** cho mọi số liệu/nội dung chương trình (đã chốt 06/08/2026).
- **IA 2 luồng** (cá nhân / coach) áp dụng nhất quán: Home, nav, footer, màu nhận diện.
- Mỗi giai đoạn xong phải được duyệt trước khi sang giai đoạn kế; riêng GĐ 2 duyệt theo từng trang.
- Việc nào chờ dữ liệu khách hàng (0.2–0.5) thì dùng placeholder `[CHỜ XÁC NHẬN]`, không chặn tiến độ.
