ALTER TABLE public.reviews
DROP CONSTRAINT reviews_pkey;
ALTER TABLE public.reviews
ADD COLUMN review_ids BIGSERIAL;
ALTER TABLE public.reviews
ADD PRIMARY KEY(review_ids);