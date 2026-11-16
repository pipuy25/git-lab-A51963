# BÁO CÁO THỰC HÀNH GIT & GITHUB WORKFLOW (git-lab-A51963)
- **Sinh viên thực hiện (Thành viên A):** Đỗ Quốc Hoàn (pipuy25)
- **Đồng đội phối hợp (Thành viên B):** Youngtun
- **Kho lưu trữ:** https://github.com/pipuy25/git-lab-A51963

---

## Phần A: Khởi tạo Git Flow & Branch Protection
- Đã khởi tạo repository với 2 nhánh chính \main\ và \develop\.
- Thiết lập Rulesets bảo vệ cả 2 nhánh: cấm push trực tiếp, bắt buộc tạo Pull Request và phải có ít nhất 1 Approving review từ Collaborator mới được merge.
- Hoàn thành PR #1 (\eature/1-calc\ -> \develop\) bằng chiến lược **Squash and merge**.

## Phần B: Quản lý công việc dở dang với Git Stash
- Khi chưa stash, chuyển nhánh sang \develop\ khiến các file đang sửa (\pp/calc.py\) và file mới (\pp/utils.py\) đi theo sang nhánh đích.
- Sử dụng \git stash push -u -m "..."\ để lưu toàn bộ thay đổi bao gồm cả file untracked, xử lý gấp nhánh \ix/3-readme\.
- Khôi phục lại thay đổi bằng \git stash apply\ (giữ nguyên bản lưu trong danh sách) và dọn dẹp thủ công bằng \git stash drop\.

## Phần C: Xử lý xung đột (Merge vs Rebase)
- Tái hiện lỗi \! [rejected] ... (fetch first)\ khi 2 thành viên cùng sửa một dòng thông báo lỗi chia cho 0 trên nhánh \eature/4-div\.
- Thử nghiệm \git pull --no-rebase\ trên nhánh nháp tạo ra lịch sử phân nhánh kèm merge commit.
- Thực hành hủy quá trình rebase an toàn bằng \git rebase --abort\ để đưa working tree về nguyên trạng.
- Giải quyết xung đột triệt để bằng \git pull --rebase\, giữ lịch sử commit trên nhánh tính năng thẳng hàng.

## Phần D: Các tình huống cứu hộ Commit (D1 – D5)
- **D1:** Sửa nội dung commit message gần nhất bằng \git commit --amend\.
- **D2:** Rút file nhạy cảm \.env\ khỏi vùng Staging bằng \git restore --staged .env\ mà không làm mất nội dung file, sau đó bổ sung vào \.gitignore\.
- **D3:** Khắc phục việc commit nhầm lên \develop\ bằng cách tách nhánh mới \eature/5-pow\ tại vị trí hiện tại rồi dùng \git reset --hard HEAD~1\ kéo \develop\ về mốc cũ.
- **D4:** Hoàn tác an toàn một commit đã merge lên remote bằng \git revert\ thông qua Pull Request mới.
- **D5:** Khôi phục 2 commit bị xóa nhầm do \git reset --hard HEAD~2\ bằng cách tra cứu lịch sử con trỏ trong \git reflog\.

## Phần E: Quy trình phát hành phiên bản & Hotfix
- **v1.0.0:** Tách \elease/1.0.0\ từ \develop\, merge vào \main\ và \develop\, gắn annotated tag \1.0.0\.
- **v1.0.1:** Tách nhánh khẩn cấp \hotfix/1.0.1\ trực tiếp từ tag \1.0.0\ để xử lý lỗi chia cho 0, merge vào cả \main\ và \develop\, gắn tag \1.0.1\, đồng thời cập nhật nhánh \eature/6-sqrt\ bằng \git rebase develop\.
- **v1.1.0:** Tích hợp tính năng \sqrt\, phát hành qua \elease/1.1.0\ và gắn tag \1.1.0\.

## Phần F: Kiểm thử tự động (Unit Testing)
- Bổ sung bộ kiểm thử đơn vị \	ests/test_calc.py\ sử dụng thư viện \unittest\ kiểm tra đầy đủ các trường hợp biên của \dd\, \sub\, \div\ và \sqrt_num\.
- Kết quả chạy \python -m unittest discover -s tests -v\: 4/4 test cases đạt trạng thái **OK**.
